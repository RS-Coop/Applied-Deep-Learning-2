# Biweekly Report 03 - Cooper Simpson

## Report Plan

1. Examine the *jiant* NLP toolkit
3. Test out some pre-trained models
4. Examine the *spaCy* NLP toolkit
5. Explore BPE like algorithms

## Goals
The purpose of this report grew out of a desire to investigate a few things in the realm of NLP. Specifically, I wanted to explore Byte Pair Encoding (BPE), the GLUE and SuperGLUE benchmarks, and large transformer models such as BERT, GPT, or XLNet. This is a lot to do on one's own, and certain tasks like trying to train a large transformer model are difficult due to resource constraints. Fortunately for me there are a wealth of NLP toolkits to facilitate the exploration of all of this topics. Such packages allow for easily working with datasets, pre-trained models, and much more. Thus I have transformed my original goals into that of examining the jiant and spaCy NLP toolkits with an emphasis on the capabilities that accomplish those original goals.

## Repository Structure

### jiant.ipynb
Investigates the jiant NLP toolkit and its use for training language models on downstream tasks.

### spacy.ipynb
Investigates the spaCy NLP toolkit and BPE like tokenization algorithms.

## Requirements
The following are required to run the code in the Jupyter Notebooks listed above. Each individual package will install a host of other dependencies, and I think it should all be covered. I would recommend building it in a new virtual environment as it results in a lot of clutter.

- [PyTorch](https://pytorch.org/)
- [jiant](https://github.com/nyu-mll/jiant)
  - NOTE: I ended up needing to install this by cloning the repository and using "pip -e .". This is outlined in their documentation if you are note familiar. It seems their pip package is not up too date, so without this the documentation does not apply in all cases.
- [spaCy](https://spacy.io/)
- [transformers](https://huggingface.co/transformers/)
- [datasets](https://huggingface.co/docs/datasets/)
- [tokenizers](https://huggingface.co/docs/tokenizers/python/latest/)
