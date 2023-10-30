import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Cleaner:
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
        cols = self.separate_data(df, '')
        for feature in cols['category']:
            for value in df[feature].unique():
                if type(value) != str and np.isnan(value):
                    continue
                new_value = value.replace('-', ' ')
                new_value = new_value.title()
                new_value = new_value.strip()
                df[feature].replace(value, new_value, inplace=True)
        return df
    
    def separate_data(self, df, target: str='', discrete_threshold=15, category_threshold=100):
        try:
            df = df.drop(target, axis=1)
        except:
            pass
        cols = {
            'target': [target],
            'time': [column for column in df.columns if df[column].dtype in ['datetime64[ns]']],
            'category': [column for column in df.columns if (df[column].dtype in ['O'])
                         and (len(df[column].unique()) <= category_threshold)],
            'category+': [column for column in df.columns if (df[column].dtype in ['O'])
                                  and (len(df[column].unique()) > category_threshold)],
            'continuous': [column for column in df.columns if (df[column].dtype in ['int64', 'float64'])
                           and (len(df[column].unique()) > discrete_threshold) and (len(df[column].unique()) != len(df))],
            'continuous+': [column for column in df.columns if (df[column].dtype in ['int64', 'float64'])
                            and (len(df[column].unique()) > discrete_threshold) and (len(df[column].unique()) == len(df))],
            'discrete': [column for column in df.columns if (df[column].dtype in ['int64', 'float64'])
                         and (len(df[column].unique()) <= discrete_threshold)],
        }
        return cols