import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_gadgets.cleaning import Cleaner


class Visualizer:
    def __init__(self, df=None):
        self.df = df
    
    def set_labels(self, title, x_label, y_label, ax):                    
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
    
    def set_data_labels(self, ax):
        for container in ax.containers:
                ax.bar_label(container, )
                
        for label in ax.texts:
            text = label.get_text()
            if text == '0':
                label.set_text('')    
    
    def clear_plots(self, fig, empty_axes):
        for ax in empty_axes:
            fig.delaxes(ax)
                                  
    def category_counts(self, df: pd.DataFrame, feature: str, ascending: bool=False, max_items: int=10, 
                        x_label=None, y_label=None, ax=None):
        if isinstance(df, pd.DataFrame):
            data = df[feature]
            
            if x_label is None:
                x_label = Cleaner().header_to_title(data.name.title())
            if y_label is None:
                y_label = 'Counts'
            
            if ax is None:
                fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
                  
            counts = data.value_counts().sort_values(ascending=ascending)
            x = counts.index[0:max_items]
            y = counts[0:max_items]
            
            if ascending:
                cmap = sns.color_palette('Reds', len(x))
            else:
                cmap = sns.color_palette('Blues_r', len(x))
                   
            sns.barplot(x=y, y=x, palette=cmap, hue=x, orient='h', legend='', ax=ax)
            self.set_labels(f'{x_label} Distribution', x_label, y_label, ax)
            self.set_data_labels(ax)
        else:
            raise ValueError('Given object is not a pandas dataframe.')
    
    def time(self, df, x, y, x_label=None, y_label=None, hue=None, estimator='mean', ax=None):
        if (isinstance(df, pd.DataFrame)):
            x = df[x]
            y = df[y]
                
            if x_label is None:
                x_label = Cleaner().header_to_title(x.name.title())
            if y_label is None:
                y_label = Cleaner().header_to_title(y.name.title())
            
            if ax is None:
                fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
                
            sns.lineplot(x=x, y=y, hue=hue, estimator=estimator, ax=ax)
            self.set_labels(f'{y_label} Trend', x_label, y_label, ax)
        else:
            raise ValueError('Given object is not a pandas dataframe.')
        
    def numerical_counts(self, df: pd.DataFrame, feature, bins='auto', kde=False , x_label=None, y_label=None, ax=None):
        if isinstance(df, pd.DataFrame):
            data = df[feature]
            
            if x_label is None:
                x_label = Cleaner().header_to_title(data.name.title())
            if y_label is None:
                y_label = 'Counts'
            
            if ax is None:
                fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
                
            sns.histplot(data, bins=bins, kde=kde, ax=ax)
            self.set_labels(f'{x_label} Distribution', x_label, y_label, ax)
            # self.set_data_labels(ax)
        else:
            raise ValueError('Given object is not a pandas dataframe.')
        
    def boxplot(self, df: pd.DataFrame, feature: str, x_label=None, ax=None):
        if isinstance(df, pd.DataFrame):
            data = df[feature] 
            
            if x_label is None:
                x_label = Cleaner().header_to_title(data.name.title())
                
            if ax is None:
                fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
                
            sns.boxplot(data, orient='h', ax=ax)
            ax.set_title(f'{x_label} Boxplot')
        else:
            raise ValueError('Given object is not a pandas dataframe.')
    
    def correlations(self, df, features: list, ax=None):
        if ax is None:
            fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
        
        sns.heatmap(data=df[features].corr(), annot=True, cmap='Blues', ax=ax)
        ax.set_title('Correlations')

    def relationship(self, df, x: str, y: str, hue=None, x_label=None, y_label=None, ax=None):
        if (isinstance(df, pd.DataFrame)):
            x = df[x]
            y = df[y]
                
            if x_label is None:
                x_label = Cleaner().header_to_title(x.name.title())
            if y_label is None:
                y_label = Cleaner().header_to_title(y.name.title())
            
            if ax is None:
                fig, ax = plt.subplots(1, 1, figsize=(19.20, 10.80))
                
            sns.scatterplot(x=x, y=y, hue=hue, ax=ax)
            self.set_labels(f'{x_label} Relationship', x_label, y_label, ax)
        else:
            raise ValueError('Given object is not a pandas dataframe.')
        
    def univariate_subplots(self, df, kind, max_rows=2, max_cols=2):
        fig, axes = plt.subplots(max_rows, max_cols, figsize=(19.20, 10.80))
        
        if max_rows <= 1 and max_cols < 2:
            raise ValueError('max_rows must be greater than 0 and max_cols must be greater than 1')
        axes = axes.flatten()
        features = df.columns[0:max_rows*max_cols]
        
        for idx, feature in enumerate(features):
            if kind == 'numerical_counts':
                self.numerical_counts(df, feature, ax=axes[idx])
            elif kind == 'category_counts':
                self.category_counts(df, feature, ax=axes[idx])
            elif kind == 'boxplot':
                self.boxplot(df, feature, ax=axes[idx])
            else:
                raise ValueError(f'{kind} is not available.')
        
        empty_axes = axes[len(features):]
        self.clear_plots(fig, empty_axes)
        
        plt.tight_layout(pad=5)
        plt.show()
        
    def multivariate_subplots(self, df, target, kind, hue=None, max_rows=2, max_cols=2):
        fig, axes = plt.subplots(max_rows, max_cols, figsize=(19.20, 10.80))
        
        axes = axes.flatten()
        features = df.drop(target, axis=1).columns[0:max_rows*max_cols]
        
        for idx, feature in enumerate(features):
            if kind == 'relationship':
                self.relationship(df, feature, target, hue=hue, ax=axes[idx])
            elif kind == 'time':
                self.time(df, target, feature, hue=hue, ax=axes[idx])
            else:
                raise ValueError(f'{kind} is not available.')
        
        empty_axes = axes[len(features):]
        self.clear_plots(fig, empty_axes)
        
        plt.tight_layout(pad=5)
        plt.show()
