#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.layers import LSTM, Embedding, Dense
from keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
import pickle
import numpy as np
import os


# In[2]:


file = open('data/eng.txt', 'r', encoding='utf8')

lines = []
for i in file:
    lines.append(i)
    
# Convert list to string
data = ''
for i in lines:
    data = ' '.join(lines)
    
data = data.replace('\n', '').replace('\r', '').replace('\ufeff', '').replace('"', '').replace("'", '')

data = data.split()
data = ' '.join(data)
data[:500]


# In[4]:


# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])

pickle.dump(tokenizer, open('token.pkl', 'wb'))

sequence_data = tokenizer.texts_to_sequences([data])[0]
sequence_data[:15]


# In[5]:


len(sequence_data)


# In[6]:


# index + 1 because index 0 will be reserved for padding
vocab_size = len(tokenizer.word_index) + 1
print(vocab_size)


# In[7]:


sequences = []

# 3 words used to predict next word
for i in range(3, len(sequence_data)):
    words = sequence_data[i-3:i+1]
    sequences.append(words)
    
print('the length of sequence are: ', len(sequences))
sequences = np.array(sequences)
sequences[:10]


# In[8]:


X = []
y = []

for i in sequences:
    X.append(i[0:3])
    y.append(i[3])
    
X = np.array(X)
y = np.array(y)


# In[9]:


print(('Data: ', X[:10]))
print(('Response: ', y[:10]))


# In[10]:


# convert class vector to binary class metrix
y = to_categorical(y, num_classes=vocab_size)
y[:5]


# In[11]:


model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=3))
model.add(LSTM(1000, return_sequences=True))
model.add(LSTM(1000))
model.add(Dense(1000, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))


# In[12]:


model.summary()


# In[47]:


from tensorflow import keras
from keras.utils.vis_utils import plot_model

keras.utils.plot_model(model, to_file='plot.png', show_layer_names=True)


# In[13]:


from tensorflow.keras.callbacks import ModelCheckpoint


# In[14]:


cheackpoint = ModelCheckpoint('next_word_eng.h5', monitor='loss', verbose=1, save_best_only=True)
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001))
model.fit(X, y, epochs=70, batch_size=64, callbacks=[cheackpoint])


# In[15]:


from tensorflow.keras.models import load_model
import numpy as np
import pickle

model = load_model('next_word_eng.h5')
tokenizer = pickle.load(open('token.pkl', 'rb'))

def predict_next_word(model, tokenizer, text):
    
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ''
    pred_list = []
    
    for key, val in tokenizer.word_index.items():
        # All Match
        pred_list.append(key)
        if val == preds:
            # Best Match
            predicted_word = key
            break
        
    print(predicted_word, pred_list)
    return predicted_word, pred_list


# In[ ]:


while(True):    
    text = input('Enter your line... ')
    
    if text == '0':
        print('Execution completed...')
        break
        
    else:
        try:
            text = text.split(' ')
            text = text[-3:]
            print(text)
            
            predict_next_word(model, tokenizer, text)
            
        except Exception as e:
            print('Error occurred: ', e)
            continue

