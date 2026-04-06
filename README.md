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

## Fortnight 1: NLP Model Inference and Evaluation

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

## Fortnight 2: Working with small, large, and classic language models

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

### 2/16: Markov Models
* [Markov Models](F2_3_MarkovModels.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F2_3_MarkovModels.ipynb)
* Further Reading
    - [Markov chain on Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
    - [NLTK Book Chapter 2: Accessing Text Corpora and Lexical Resources](https://www.nltk.org/book/ch02.html)
    - [What is ChatGPT Doing and Why Does it Work? By Stephen Wolfram](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)
        * This is a fascinating article that covers a lot of NLP topics. The opening motivates text generation with Markov-like descriptions.
    - [Chapter 3: N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf). *Speech and Language Processing.* Daniel Jurafsky & James H. Martin

### 2/18: Subword Tokenization and Byte-Pair Encoding
* [Subword Tokenization and Byte-Pair Encoding](F2_4_SubwordTokenizationBPE.ipynb)[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F2_4_SubwordTokenizationBPE.ipynb)
* Further Reading
    - [GPT Tokenizer Illustration](https://platform.openai.com/tokenizer)
    - [Hugging Face Byte-Pair Encoding tokenization](https://huggingface.co/learn/nlp-course/chapter6/5?fw=pt)
    - [Chapter 2: Words and Tokens](https://web.stanford.edu/~jurafsky/slp3/2.pdf). *Speech and Language Processing.* Daniel Jurafsky & James H. Martin
    - Python resources for retrieving and tokenizing text data:
        * [Python `requests` library quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
        * [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
        * [Python `split` method](https://docs.python.org/3/library/stdtypes.html#str.split)

---

## Fortnight 3: Machine Learning with Text

### 2/23: Industry Partner Use of NLP and Demo Day
* Presentation from Berkshire Hathaway Energy: Vinay Kodigante, Ryan Blokhuis, Amanda Pereira
* Demo Day
    - 5-min demo of creative synthesis project or completed applied exploration (or core practice if that's what you have)
    - Write down the names of the people you presented to
    - (optional) Nominate a cool project to show off to everyone
* [Sample Portfolio in Google Drive + Colab](https://drive.google.com/drive/folders/1RKWq7TQq3QgakAPlykTQbmIgEx_HQ8Fm?usp=drive_link)

### 2/25: Machine Learning with Text Data
* [Machine Learning with Text Data](F3_1_MachineLearning.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F3_1_MachineLearning.ipynb)
* Further Reading
    - [Chapter 11: Information Retrieval and Retrieval-Augmented Generation](https://web.stanford.edu/~jurafsky/slp3/11.pdf). *Speech and Language Processing.* Daniel Jurafsky & James H. Martin
    - [scikit-learn API reference](https://scikit-learn.org/stable/modules/classes.html)
    - [Professor Urness' Machine Learning material from Fall 2025](https://github.com/urness/CS167Fall2025)

### 3/2: Review of Logistic Regression and Optimization, Introduction to PyTorch
* [Review of Logistic Regression and Optimization, Introduction to PyTorch](F3_2_LogisticRegressionPyTorch.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F3_2_LogisticRegressionPyTorch.ipynb)
* Further Reading
    - [Chapter 4: Logistic Regression and Text Classificationn](https://web.stanford.edu/~jurafsky/slp3/4.pdf). *Speech and Language Processing.* Daniel Jurafsky & James H. Martin


### 3/4: Multiclass PyTorch, Adam, and Neural Networks
* [Multiclass PyTorch, Adam, and Neural Networks](F3_3_MulticlassAdamNeuralNetworks.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F3_3_MulticlassAdamNeuralNetworks.ipynb)
* Further Reading
    - [SLP: Neural Networks, Chapter 6 of Speech and Language Processing by Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/6.pdf)
    - [Adam vs SGD : What are the optimizers in neural network and when do we use? by Adam Lee](https://medium.com/@pumadd1227/adam-vs-sgd-what-are-the-optimizers-in-neural-network-and-when-do-we-use-238478a0eaea)
    - [Artificial Neural Networks, Chapter 4 of Machine Learning by Tom M. Mitchell](http://www.cs.cmu.edu/~tom/files/MachineLearningTomMitchell.pdf)
    - [PyTorch CrossEntropyLoss reference](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)
    - [PyTorch Sequential model reference](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sequential.html)

---

## Fortnight 4: Embeddings

### 3/9: Demo Day and Embeddings
* Demo Day
    - 5-min demo of creative synthesis project or completed applied exploration (or core practice if that's what you have)
    - Write down the names of the people you presented to
    - (optional) Nominate a cool project to show off to everyone
* [Embeddings](F4_1_Embeddings.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F4_1_Embeddings.ipynb)
* Further Reading
    - [SLP: Embeddings, Chapter 5 of Speech and Language Processing by Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/5.pdf)
    - [Word2Vec Tutorial - The Skip-Gram Model by Chris McCormick](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
    - [Word2Vec - Negative Sampling made easy by Munesh Lakhey](https://medium.com/@mnshonco/word2vec-negative-sampling-made-easy-9a587cb4695f)
    - [PyTorch `nn.Embedding` documentation](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)
    - [PyTorch `torch.nn.functional.one_hot` documentation](https://pytorch.org/docs/stable/generated/torch.nn.functional.one_hot.html)

### 3/11: PyTorch Embeddings
* [PyTorch Embeddings](F4_2_PyTorchEmbeddings.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F4_2_PyTorchEmbeddings.ipynb)
* Further Reading: Same as previous notes


### 3/23: No class due to Eric speaking at a conference
* See announcement email


### 3/25: Semantic Search with Embeddings
* [Semantic Search with Embeddings](F4_3_SemanticSearchEmbeddings.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F4_3_SemanticSearchEmbeddings.ipynb)
    * Further Reading:
        - [Dot product (Wikipedia)](https://en.wikipedia.org/wiki/Dot_product)
        - [Cosine similarity (Wikipedia)](https://en.wikipedia.org/wiki/Cosine_similarity)
        - [Sentence-Transformers documentation](https://www.sbert.net/)
        - [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)


---

## Fortnight 5: RAG, More on Similarity, and Neural Language Modeling

### 3/30: Demo Day and Retrival Augmented Generation (RAG)
* Demo Day
    - 5-min demo of creative synthesis project or completed applied exploration (or core practice if that's what you have)
    - Write down the names of the people you presented to
    - (optional) Nominate a cool project to show off to everyone
* [Retrieval Augmented Generation](F5_1_RAG.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F5_1_RAG.ipynb)
* Further Reading
    - [Hugging Face Chat Basics](https://huggingface.co/docs/transformers/en/conversations)
    - [Sentence-Transformers documentation](https://www.sbert.net/)
    - [SLP: Information Retrieval and Retrieval-Augmented Generation, Chapter 11 of Speech and Language Processing by Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/11.pdf)

### 4/1: Evan Scherrer presents WordNet
* [Semantic Similarity with WordNet](https://github.com/ericmanley/S26-CS195NLP/blob/main/F5_2_Evan_Scherrer_Wordnet.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F5_2_Evan_Scherrer_Wordnet.ipynb)
* Further Reading
    - [WordNet Homepage](https://wordnet.princeton.edu/)
    - [Wordnet on Wikipedia](https://en.wikipedia.org/wiki/WordNet)
    - [WordNet sample usage with Python](https://www.nltk.org/howto/wordnet.html)
    - [WordNet glossary of terms](https://wordnet.princeton.edu/documentation/wngloss7wn)
    - [Intro to WordNet with Python NLTK](https://medium.com/@don_khozzy/dive-into-wordnet-with-nltk-b313c480e788)

### 4/6: Recurrent Neural Networks and Language Modeling
* [Recurrent Neural Networks and Language Modeling](https://github.com/ericmanley/S26-CS195NLP/blob/main/F5_3_RNNLanguageModels.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ericmanley/s26-CS195NLP/blob/main/F5_3_RNNLanguageModels.ipynb)
* Further Reading
    - [SLP: N-gram Language Models, Chapter 3 of Speech and Language Processing by Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
    - [SLP: RNNs and LSTMs, Chapter 13 of Speech and Language Processing by Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/13.pdf)
    - [PyTorch `nn.RNN` docs](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)
    - [PyTorch `nn.Embedding` docs](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)



