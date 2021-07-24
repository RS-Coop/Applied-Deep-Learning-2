# Biweekly Report 06 - Cooper Simpson

## Report Plan
1. Audio dataset investigation
  - Spoken Digit data exploration
  - Mel-Spectrogram and Mel-Frequency Cepstral Coefficients
  - Data augmentation techniques
2. Music classification
  - gtzan dataset

## Goals and Results
The goal of this report was to get familiar working with audio data and using it in a deep learning setting. First, I investigated the Spoken Word dataset which serves as a good model for loading, processing, and examining audio data. Next, I went through the process of converting raw audio data into Mel-scale spectrograms and extracting MFCCs. With this spectrograms I also tested out some simple data augmentation techniques which are often useful in deep learning. Lastly, I applied what I had learned to a practical task of classifying audio data as one of a number of genres using the gtzan dataset.

Altogether I feel I have accomplished my goal of introducing myself to audio based deep learning. I would have liked to go a little further and examine some more state-of-the-art models like wav2vec 2.0, but I can save that for the future.

## Repository Structure
- *Audio Data Exploration*: This Jupyter Notebook covers the first part of my report plan.
- *Simple Audio Recognition*: This Jupyter Notebook covers the second part of my report plan.

## Requirements
Beyond standard scientific computing Python packages the following are required.

- tensorflow
- tensorflow_datasets
- tensorflow-io
