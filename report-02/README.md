# Biweekly Report 02 - Cooper Simpson

## Report Plan
1. Investigate the Large Movie Reviews Dataset otherwise known as the imdb reviews dataset.
2. Train a variety of neural network architechtures on the imdb dataset and compare them.
    - Dense
    - CNN
    - RNN

## Goals and Results
The goal of this report was to further investigate text datasets and become more adept with neural network models for text-based tasks. I succeeded on all fronts, although I would have liked to do more on the model side. In the future I will try to integrate more pre-exisiting components to make things faster, easier, and allow for more depth in my investigations.

## Repo Structure

### IMDB Reviews - Exploratory Data Analysis.ipynb
This notebook explores the imdb reviews dataset and helps inform various tasks in the following notebook.

### Document Classification Models.ipynb
In this notebook I use the imdb reviews dataset to examine the task of text-based binary sentiment classification. I look at three different model architechtures to see how their performance and other qualities vary.

### imdb
This folder is where the imdb reviews dataset will be downloaded when using tensorflow datasets. Subsequent calls will reuse this data.

## Requirements
- tensorflow
- tensorflow_datasets
- nltk
- matplotlib, pandas, numpy, seaborn
- imdb dataset: Download in associated notebook