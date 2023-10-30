import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_gadgets.cleaning import Cleaner
from data_gadgets.visualization import Visualizer

clean = Cleaner()
visualize = Visualizer()

data = pd.read_csv('data/raw/data_task1.csv')
# data = data.drop('Unnamed: 0', axis=1)
        
# data = clean.feature_names(data)
# data = clean.categories(data)
# print(data.head())

visualize.univariate_subplots(data[['Age']], 'boxplot', 1, 2)