import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.utils.clean import Clean
class Visualize:
    def __init__(self, df=None):
        self.df = df
        
    def plot_counts(self, df_feature: pd.Series, ascending: bool=False, max_items: int=10, x_label=None):
        if isinstance(df_feature, pd.Series):
            if x_label is None:
                x_label = Clean().header_to_title(df_feature.name.title())
            
            counts = df_feature.value_counts().sort_values(ascending=ascending)
            x = counts.index[0:max_items]
            y = counts[0:max_items]
            
            if ascending:
                rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))
                cmap = plt.get_cmap('Reds_r')
                cmap = cmap(rescale(y))
            else:
                rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))
                cmap = plt.get_cmap('Blues')
                cmap = cmap(rescale(y))
            
            plt.figure(figsize=(20,8))
            plt.barh(x, y, color=cmap)
            plt.gca().invert_yaxis()
            plt.xlabel(x_label)
            plt.ylabel('Counts')
            plt.title(f'{x_label} Counts')
        
            plt.show()
        else:
            raise ValueError('Given object is not a pandas series.')
        