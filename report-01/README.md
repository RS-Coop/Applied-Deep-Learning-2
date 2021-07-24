# Biweekly Report 01 - Cooper Simpson

## Report Plan
1. Download and access the ag_news_subset
2. Investigate and explore this dataset
3. Prepare this dataset for use in deep learning task

## Goals and Results
The goal of this first report was to try out some of the various word embedding techniques we have learned about. Unfortunately, I didn't quite get there as a I spent most of my time on dataset analysis and processing. I feel much more confident working with these text datasets, and the work I have done for this first report will greatly speed up any subsequent data tasks for future reports. Thus I can now focus more on the deep learning, or quickly analyze new datasets.

## Repo Structure

### Dataset.ipynb
A thorough investigation into the ag_news_subset dataset and data preparation tasks for deep learning.

### data_csv
This folder is for the manually downloaded ag_news_subset dataset. More info on how to do this manual download can be found in the Requirements section.

### data_tf
This folder if for the TensorFlow Datasets download of the ag_news_subset. This can supposedly be downloaded using TF Datasets functionality, but I had to implement a workaround. More info on this can be found in the Requirements section

## Requirements
- tensorflow
- tensorflow_datasets (not actually required if you do manual download)
- numpy
- pandas
- seaborn & matplotlib
- ag_news_subset
    - TF Datasets should be fixed, see notebook for more details
    - [Manual download](https://drive.google.com/uc?export=download&id=0Bz8a_Dbh9QhbUDNpeUdjb0wxRms), Then extract to *data_csv*
    - CLI Workaround: See notebook for details

