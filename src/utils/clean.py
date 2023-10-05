import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Clean:
    def __init__(self, df=None):
        self.df = df
    
    def headers(self, df):
        new_feature_names = []
        for feature in df.columns:
            feature = feature.lower()
            feature = feature.strip()
            feature = feature.replace(' ', '_')
            new_feature_names.append(feature)
            
        df.columns = new_feature_names
        
        return df
    
    def header_to_title(self, header):
        header = header.replace('_', ' ')
        header = header.title()
        
        return header

    def categories(self, df):
        for feature in df.columns:
            for value in df[feature].unique():
                if type(value) is not str and np.isnan(value):
                    continue
                new_value = value.replace('-', ' ')
                new_value = new_value.title()
                new_value = new_value.strip()
                df[feature].replace(value, new_value, inplace=True)
        return df
    
    def separate_data(self, df, discrete_threshold=15):
        cols = {
            'time': [column for column in data.columns if df[column].dtype in ['datetime64[ns]']],
            'category': [column for column in data.columns if df[column].dtype in ['O']],
            'continuous': [column for column in data.columns if (df[column].dtype in ['int64', 'float64'])
                        and (len(df[column].unique()) > discrete_threshold)],
            'discrete': [column for column in data.columns if (df[column].dtype in ['int64', 'float64'])
                        and (len(df[column].unique()) <= discrete_threshold)],
        }
        return cols