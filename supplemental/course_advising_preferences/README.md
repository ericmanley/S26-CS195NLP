# Course Advising RAG Candidate Data

This folder contains supplemental data-building code for the F7_2 alignment activity.
It is not intended to be a class-facing notebook.

- `course_advising_questions.jsonl` has editable student-style questions.
- `course_advising_unsupported_questions.json` has targeted questions where the
  retrieved course context is unlikely to contain enough information.
- `generate_rag_candidates.py` runs the F5_1-style RAG pipeline and writes raw answer candidates.

From the repository root, run:

```bash
python3 supplemental/course_advising_preferences/generate_rag_candidates.py --overwrite
```

The default output is:

```text
data/course_advising_rag_candidates.jsonl
```

If the output path ends in `.json`, the script writes a pretty-printed JSON
array instead of JSONL. That format is easier to inspect by hand:

```bash
python3 supplemental/course_advising_preferences/generate_rag_candidates.py \
  --questions supplemental/course_advising_preferences/course_advising_unsupported_questions.json \
  --output data/course_advising_unsupported_rag_candidates.json \
  --overwrite
```

By default, the script uses `Qwen/Qwen2.5-0.5B-Instruct` for generation. It
generates two answers for each question using different temperatures:

- `answer_a`: lower temperature, default `0.2`
- `answer_b`: higher temperature, default `0.9`

You can change those with `--temperature-a` and `--temperature-b`.

For a quick smoke test with only a few questions:

```bash
python3 supplemental/course_advising_preferences/generate_rag_candidates.py --limit 3 --overwrite
```

The generated file is intentionally unlabeled. After inspecting the two answers for each question, we can decide which answer should become `chosen` and which should become `rejected` for DPO.

The combined shareable preference dataset is:

```text
data/course_advising_dpo_preferences.json
```

It includes metadata and review notes. For code that only needs TRL's basic DPO
fields, use:

```text
data/course_advising_dpo_preferences_trl.json
```
