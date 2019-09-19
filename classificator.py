import numpy as np 
import pandas as pd 

import tensorflow as tf 
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('position')
  dataframe.pop('name')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  #print(labels)
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

dataframe = pd.read_csv('playerDataSet.csv', engine='python', encoding='ISO-8859-1', error_bad_lines=False)
<<<<<<< HEAD
print(dataframe.head())
print('Hola a todos')
=======
print(dataframe.dtypes)

target = dataframe.pop('position')


dataset = tf.data.Dataset.from_tensor_slices((dataframe.values, target.values))

for feature, targ in dataset.take(5):
    print('Features: {}, Target: {}'.format(feature, targ))

#print(dataframe.head())
""" 
train, test = train_test_split(dataframe, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)

print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')

batch_size = 1 # A small batch sized is used for demonstration purposes
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)

for feature_batch, label_batch in train_ds.take(1):
  print('Every feature:', list(feature_batch.keys()))
  print('A batch of dribbling:', feature_batch['dribbling'])
  print('A batch of targets:', label_batch ) """
>>>>>>> dbde8fece57d4f8552a57ef63fa2d01ef5a17bae
