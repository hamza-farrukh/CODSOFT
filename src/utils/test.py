import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.utils.clean import Clean
from src.utils.visualize import Visualize

clean = Clean()
visualize = Visualize()

data = pd.read_csv('data/raw/data.csv')
data = data.drop('Unnamed: 0', axis=1)
        
# data = clean.feature_names(data)
data = clean.categories(data)
print(data.head())

# visualize.plot_counts(data['degrees'], ascending=False, max_items=10)
