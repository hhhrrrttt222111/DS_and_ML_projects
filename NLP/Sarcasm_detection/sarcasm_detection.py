# The objetive of this projects is identify sarcasm words, we sill use this DS https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection/

# 1. Import libraries and charge data

import itertools

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import nltk

## Configure NLTK
nltk.download('punkt')
nltk.download('stopwords')

dataset = pd.read_json('Sarcasm_Headlines_Dataset.json', lines= True)
dataset.headline[500]
dataset.shape
sns.countplot(dataset.is_sarcastic)
plt.show()

# 2. Explore Data

index_random = np.random.randint(0,high = dataset.shape[0])
titular = dataset.iloc[index_random].headline
print(index_random, titular)

print(index_random, dataset.iloc[index_random].is_sarcastic)

# 3. NLTK

## 3.1 NLTK  - Token

titular_st = nltk.tokenize.sent_tokenize(titular)
titular_st

titular_wt = nltk.tokenize.word_tokenize(titular)
titular_wt
