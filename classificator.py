import numpy as np 
import pandas as pd 

import tensorflow as tf 
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

dataframe = pd.read_csv('playerDataSet.csv', engine='python', encoding='ISO-8859-1', error_bad_lines=False)
print(dataframe.head())
print('Hola a todos')