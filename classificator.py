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
print(dataframe.head())
print('Hola a todos')
