# Biweekly Report 04 - Cooper Simpson

## Report Plan
1. Investigate the XNLI dataset
  - Examine the dataset itself
  - Use the dataset on a pre-trained model
2. Hard attention
  - Work through the derivation
  - Describe connections to Reinforcement Learning

## Goals and Results
I have two distinct goals for this report that are quite different from each other. First, I want to look at the XNLI dataset and use it in some pre-trained model. I have yet to look at a cross lingual dataset, and after the fiasco with Jiant last time I would like to get a little more familiar with Hugging Face. Second, I want to work through Hard Attention on my own. I think the whole idea is very interesting, and it has some important subtleties that I want to better understand. Specifically, some of the probability tricks and the RL connection seem useful.

In both of this endeavors I think I was successful. Most importantly to me I have a much better understanding of Hard attention, and I am excited to dive deeper into RL.

## Repository Structure
- *XNLI - Dataset Investigation*: Jupyter Notebook for dataset investigation and working with pre-trained model
- *Hard Attention*: Hard attention derivation and discussion
- *data*: Location for download XNLI data

## Requirements
- pytorch
- sentencepiece
- [transformers](https://huggingface.co/transformers/)
- [datasets](https://huggingface.co/docs/datasets/)
