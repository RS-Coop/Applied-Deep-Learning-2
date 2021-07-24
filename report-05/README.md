# Biweekly Report 05 - Cooper Simpson

## Report Plan
For the following plan I will define "investigate" as follows:
  - Work through the background math
  - Implement in TensorFlow on simple MNIST dataset

1. Investigate Variational Auto-Encoders
2. Investigate standard GANs

## Goals and Results
For this report my overarching goal is to better understand the math behind two types of generative networks, and to gain experience implementing them in a practical setting. Specifically, I consider Variational Auto-Encoders, and traditional Generative Adversarial Networks -- trained on the MNIST handwritten digits dataset.

For VAEs I have achieved a much better understanding of their mathematical formulation, which I feel is quite valuable. With both model types I think I have made a bit of a breakthrough in my understanding and skills with TensorFlow. I certainly feel much more comfortable working with custom model definitions and training.

I would like to continue working with GANs specifically to examine the multitude of methods and tricks for training. As well, I would like to examine some of the major variants like Wasserstein GANs and Conditional GANs.

## Repository Structure
- *Variational Auto-Encoders*: A notebook examining VAEs
- *Generatve Adversarial Networks*: A notebook examining GANS

## Requirements
- tensorflow
- tensorflow probability
