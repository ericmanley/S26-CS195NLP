"""Generate raw RAG answer candidates for course-advising preference data.

This script mirrors the core RAG flow from F5_1_RAG.ipynb:

1. Load Drake course records.
2. Convert each record to plain text.
3. Embed records with sentence-transformers/all-MiniLM-L6-v2.
4. Retrieve the top-k records for each student question.
5. Ask a chat model to answer using the retrieved context.

The output is intentionally unlabeled. It gives us question/context/answer pairs
we can inspect before deciding which responses should be preferred or rejected.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch
from sentence_transformers import SentenceTransformer
from transformers import pipeline, set_seed
from transformers.utils import logging as hf_logging


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_COURSE_DATA = REPO_ROOT / "data" / "f25_course_information.json"
DEFAULT_QUESTIONS = Path(__file__).with_name("course_advising_questions.jsonl")
DEFAULT_OUTPUT = REPO_ROOT / "data" / "course_advising_rag_candidates.jsonl"

DEFAULT_RETRIEVAL_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_GENERATION_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

SYSTEM_PROMPT = (
    "You are a careful course advising assistant. "
    "Use only the retrieved Drake course information. "
    "Do not use outside knowledge about other universities or course catalogs. "
    "Do not invent instructors, meeting times, prerequisites, locations, or requirements. "
    "Include course numbers and titles when they are relevant. "
    "For topic questions, recommend a course only when its title or description explicitly matches the requested topic. "
    "If the same course appears in multiple sections, treat it as one course unless the question asks about sections or meeting times. "
    "Do not recommend a course just because it was retrieved; use it only if it directly answers the question. "
    "If one retrieved course clearly answers the question, lead with that course and avoid loosely related extras. "
    "If the answer is not supported by the retrieved context, say that you do not know "
    "based on the provided course information."
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_questions(path: Path) -> list[dict[str, Any]]:
    if path.suffix == ".json":
        data = load_json(path)
        if not isinstance(data, list):
            raise ValueError(f"Expected a list of question objects in {path}")
        return data

    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on {path}:{line_number}") from exc
    return rows


def write_rows(path: Path, rows: list[dict[str, Any]], append: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".json":
        if append and path.exists():
            existing = load_json(path)
            if not isinstance(existing, list):
                raise ValueError(f"Expected a list in existing output file {path}")
            rows = existing + rows
        with path.open("w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
            f.write("\n")
        return

    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def course_record_to_text(record: dict[str, Any]) -> str:
    faculty = ", ".join(record.get("faculty") or [])
    attributes = ", ".join(record.get("attributes") or [])
    location = ", ".join(record.get("location") or [])
    times = ", ".join(record.get("times") or [])

    parts = [
        f"Course: {record.get('course_number', '')}",
        f"Subject: {record.get('subject', '')}",
        f"Title: {record.get('title', '')}",
        f"Description: {record.get('description', '').strip()}",
        f"Prerequisites: {record.get('prereq', '')}",
        f"Faculty: {faculty}",
        f"Attributes: {attributes}",
        f"Location: {location}",
        f"Times: {times}",
    ]
    return "\n".join(parts)


def cosine(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return torch.dot(a, b) / (torch.norm(a) * torch.norm(b))


def retrieve_documents(
    query: str,
    records: list[dict[str, Any]],
    documents: list[str],
    doc_embeddings: torch.Tensor,
    retrieval_model: SentenceTransformer,
    top_k: int = 3,
) -> list[dict[str, Any]]:
    query_embedding = retrieval_model.encode(query, convert_to_tensor=True)

    scores = []
    for d_idx in range(len(documents)):
        doc_sim_score = cosine(query_embedding, doc_embeddings[d_idx])
        scores.append(doc_sim_score)

    top_idx = torch.topk(torch.tensor(scores), k=top_k).indices.tolist()

    results = []
    for idx in top_idx:
        record = records[idx]
        results.append(
            {
                "score": scores[idx].item(),
                "course_number": record.get("course_number"),
                "subject": record.get("subject"),
                "title": record.get("title"),
                "faculty": record.get("faculty"),
                "times": record.get("times"),
                "location": record.get("location"),
                "attributes": record.get("attributes"),
                "filename": record.get("filename"),
                "document": documents[idx],
            }
        )
    return results


def format_retrieved_context(retrieved: list[dict[str, Any]]) -> str:
    grouped = []
    grouped_index = {}
    for hit in retrieved:
        key = (hit.get("course_number"), hit.get("title"))
        if key not in grouped_index:
            grouped_index[key] = len(grouped)
            grouped.append({**hit, "additional_sections": []})
        else:
            grouped[grouped_index[key]]["additional_sections"].append(
                {
                    "faculty": hit.get("faculty"),
                    "times": hit.get("times"),
                    "location": hit.get("location"),
                    "score": hit.get("score"),
                }
            )

    blocks = []
    for idx, hit in enumerate(grouped, start=1):
        lines = [
            f"Retrieved course {idx} (similarity score: {hit['score']:.3f})",
            hit["document"],
        ]
        for section in hit["additional_sections"]:
            lines.append(
                "Additional retrieved section: "
                f"Faculty: {section['faculty']}; "
                f"Times: {section['times']}; "
                f"Location: {section['location']}; "
                f"similarity score: {section['score']:.3f}"
            )
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def make_rag_messages(
    question: str,
    retrieved: list[dict[str, Any]],
    extra_instruction: str = "",
) -> list[dict[str, str]]:
    context = format_retrieved_context(retrieved)
    system_prompt = SYSTEM_PROMPT
    if extra_instruction:
        system_prompt = f"{system_prompt} {extra_instruction}"

    return [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": (
                f"Question: {question}\n\n"
                f"Retrieved course information:\n{context}\n\n"
                "Answer the question using only the retrieved course information. "
                "Focus on courses that directly answer the question, and briefly explain why they match."
            ),
        },
    ]


def answer_question(
    chatbot: Any,
    question: str,
    retrieved: list[dict[str, Any]],
    max_new_tokens: int,
    temperature: float,
    top_p: float,
    seed: int,
    extra_instruction: str = "",
) -> str:
    set_seed(seed)
    messages = make_rag_messages(question, retrieved, extra_instruction=extra_instruction)
    response = chatbot(
        messages,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
    )
    return response[0]["generated_text"][-1]["content"].strip()


def build_candidate_rows(
    questions: list[dict[str, Any]],
    records: list[dict[str, Any]],
    retrieval_model_name: str,
    generation_model_name: str,
    top_k: int,
    max_new_tokens: int,
    temperature_a: float,
    temperature_b: float,
    top_p: float,
    seed: int,
    limit: int | None,
    answer_a_extra_instruction: str,
    answer_b_extra_instruction: str,
) -> list[dict[str, Any]]:
    if limit is not None:
        questions = questions[:limit]

    course_texts = [course_record_to_text(record) for record in records]

    retrieval_model = SentenceTransformer(retrieval_model_name)
    course_embeddings = retrieval_model.encode(course_texts, convert_to_tensor=True)

    chatbot = pipeline(
        "text-generation",
        model=generation_model_name,
        dtype="auto",
        device_map="auto",
    )

    rows = []
    for q_idx, question_row in enumerate(questions, start=1):
        question = question_row["question"]
        print(f"[{q_idx}/{len(questions)}] {question_row['id']}: {question}", flush=True)

        retrieved = retrieve_documents(
            question,
            records,
            course_texts,
            course_embeddings,
            retrieval_model,
            top_k=top_k,
        )

        answer_a = answer_question(
            chatbot,
            question,
            retrieved,
            max_new_tokens=max_new_tokens,
            temperature=temperature_a,
            top_p=top_p,
            seed=seed + q_idx * 2,
            extra_instruction=answer_a_extra_instruction,
        )
        answer_b = answer_question(
            chatbot,
            question,
            retrieved,
            max_new_tokens=max_new_tokens,
            temperature=temperature_b,
            top_p=top_p,
            seed=seed + q_idx * 2 + 1,
            extra_instruction=answer_b_extra_instruction,
        )

        rows.append(
            {
                "id": question_row["id"],
                "category": question_row.get("category"),
                "question": question,
                "retrieved_context": retrieved,
                "answer_a": answer_a,
                "answer_b": answer_b,
                "metadata": {
                    "retrieval_model": retrieval_model_name,
                    "generation_model": generation_model_name,
                    "top_k": top_k,
                    "max_new_tokens": max_new_tokens,
                    "temperature_a": temperature_a,
                    "temperature_b": temperature_b,
                    "top_p": top_p,
                    "seed": seed,
                    "answer_a_extra_instruction": answer_a_extra_instruction,
                    "answer_b_extra_instruction": answer_b_extra_instruction,
                },
            }
        )

    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate raw RAG answer candidates for course-advising DPO data."
    )
    parser.add_argument("--course-data", type=Path, default=DEFAULT_COURSE_DATA)
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--retrieval-model", default=DEFAULT_RETRIEVAL_MODEL)
    parser.add_argument("--generation-model", default=DEFAULT_GENERATION_MODEL)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--max-new-tokens", type=int, default=180)
    parser.add_argument("--temperature-a", type=float, default=0.2)
    parser.add_argument("--temperature-b", type=float, default=0.9)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument("--seed", type=int, default=195)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--answer-a-extra-instruction", default="")
    parser.add_argument("--answer-b-extra-instruction", default="")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace the output file instead of appending to it.",
    )
    return parser.parse_args()


def main() -> None:
    hf_logging.set_verbosity_error()
    args = parse_args()

    records = load_json(args.course_data)
    questions = load_questions(args.questions)

    rows = build_candidate_rows(
        questions=questions,
        records=records,
        retrieval_model_name=args.retrieval_model,
        generation_model_name=args.generation_model,
        top_k=args.top_k,
        max_new_tokens=args.max_new_tokens,
        temperature_a=args.temperature_a,
        temperature_b=args.temperature_b,
        top_p=args.top_p,
        seed=args.seed,
        limit=args.limit,
        answer_a_extra_instruction=args.answer_a_extra_instruction,
        answer_b_extra_instruction=args.answer_b_extra_instruction,
    )
    write_rows(args.output, rows, append=not args.overwrite)
    print(f"Wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
