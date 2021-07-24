'''
Functionality for loading ag_news_subset dataset

This dataset is pretty small, so the way I am doing it here works well,
but for larger datasets there are certainly better ways to do it.
'''

from os.path import join
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from nltk.corpus import stopwords

def clean_text(text, stopwords=False):
    #Convert to lower case
    text = text.lower()

    #Remove punctuation
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)

    if stopwords==True:
        text = [word for word in text.split() if word not in stopwords.words('english')]
        return ' '.join(text)

    else:
        return text

#Load the ag_news_subset
class AGNews():
    classes = ['World', 'Sports', 'Business', 'Science/Technology']

    def __init__(data_path):
        self.data_path = data_path

    def loadDataset(split='train'):
        assert split in ['train', 'test']

        df = pd.read_csv(join(self.data_dir, split+'.csv'), 
                                names=['Label', 'Title', 'Description'])

        df1 = df[['Label','Title']]
        df2 = df[['Label','Description']]

        df1.columns = ['Label', 'Text']
        df2.columns = ['Label', 'Text']

        df = pd.concat([df1,df2], ignore_index=True)

        df['Text'] = df['Text'].apply(lambda x: clean_text(x))
        df['Label'] = df['Label'].apply(lambda x: x-1)

        y = to_categorical(df['Label'])

        return tf.data.Dataset.from_tensor_slices((df['Text'], y))