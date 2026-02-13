# CS 195: Natural Language Processing
**Spring 2026**

## Instructor

Eric Manley

 :speech_balloon: [Microsoft Teams](https://teams.microsoft.com/l/chat/0/0?users=eric.manley@drake.edu)

:email: eric.manley@drake.edu

:office: Collier-Scripps 327


### Office Hours

:calendar: Schedule in [Calendly](https://calendly.com/eric-manley/office-hours) the day before or drop in
* MW 9:30 - 12:00pm


---

## Fortnight 1

### 1/26 Prologue: Adventure Awaits
* [Syllabus](F0_0_Syllabus.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F0_0_Syllabus.ipynb)
* [Gonzalo's Example Portfolio](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/tree/main)
    - Note that Gonzalo removed info about xp earned and group-members presented to for his public portfolio, but you should include them.
* [Sign up for Colab Pro (free for students)](https://colab.research.google.com/signup)


### 1/28: Using the Transformers Library
* [Introduction to Hugging Face Transformers Library](F1_1_HuggingFace.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F1_1_HuggingFace.ipynb)
* Further Reading
    - [Hugging Face *Quicktour*](https://huggingface.co/docs/transformers/quicktour)
    - [Hugging Face *Run Inference with Pipelines tutorial*](https://huggingface.co/docs/transformers/pipeline_tutorial)
    - [Hugging Face *NLP Course, Chapter 2*](https://huggingface.co/learn/nlp-course/chapter2/1)


### 2/2: Text Classification Data and Evaluation
* [Loading Data and Evaluating Classification Models](F1_2_DataEvaluation.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F1_2_DataEvaluation.ipynb)
* Further Reading
    - [Hugging Face Load a dataset from the Hub tutorial](https://huggingface.co/docs/datasets/load_hub)
    - [Arrow for datasets](https://huggingface.co/docs/datasets/about_arrow)
    - [scikit-learn Classification Metrics User's Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)

### 2/4: ROUGE and Summarization
* [ROUGE and Summarization](F1_3_RougeSummarization.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F1_3_RougeSummarization.ipynb)
* Further Reading
    - [*Two minutes NLP — Learn the ROUGE metric* by examples](https://medium.com/nlplanet/two-minutes-nlp-learn-the-rouge-metric-by-examples-f179cc285499) by Fabio Chiusan 
    - [Google's implementation of rouge_score](https://github.com/google-research/google-research/tree/master/rouge)
    - [Hugging Face's wrapper for Google's implementation](https://huggingface.co/spaces/evaluate-metric/rouge)
    - [Hugging Face Task Guide on Summarization](https://huggingface.co/docs/transformers/tasks/summarization)


---

## Fortnight 2

### 2/9: Demo Day, Chat & Instruct Models
* Demo Day
    - 5-min demo of creative synthesis project or completed applied exploration (or core practice if that's what you have)
    - Write down the names of the people you presented to
    - (optional) Nominate a cool project to show off to everyone
* [Chat and Instruct Models](F2_1_ChatInstruct.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F2_1_ChatInstruct.ipynb)
* Further Reading
    - [Hugging Face Chat Basics](https://huggingface.co/docs/transformers/en/conversations)
    - [SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model](https://arxiv.org/pdf/2502.02737)


### 2/11: Large Language Models via Web API
* [Large Language Models via Web API](F2_1_ChatInstruct.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F2_2_LLMAPI.ipynb)
* Further Reading
    - [Hugging Face Chat Basics](https://huggingface.co/docs/transformers/en/conversations)
    - [OpenAI Developer Quickstart](https://developers.openai.com/api/docs/quickstart)

### 2/17: Markov Models
* [Markov Models](F2_3_MarkovModels.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F2_3_MarkovModels.ipynb)
* Further Reading
    - [Markov chain on Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
    - [NLTK Book Chapter 2: Accessing Text Corpora and Lexical Resources](https://www.nltk.org/book/ch02.html)
    - [What is ChatGPT Doing and Why Does it Work? By Stephen Wolfram](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)
        * This is a fascinating article that covers a lot of NLP topics. The opening motivates text generation with Markov-like descriptions.
    - [Chapter 3: N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf). *Speech and Language Processing.* Daniel Jurafsky & James H. Martin
