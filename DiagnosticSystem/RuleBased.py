import pickle
import pandas as pd
from statistics import mean, stdev

nuclei_index = ['_0' ,'_1','_2']


def define_rule(param):
    return lambda x: x[param] >= get_threshold(param), 1

def get_threshold(param_name):
    malignant_average = mean([x[param_name] for _,x in data_df.iterrows() if x['malignant']])
    benign_average = mean([x[param_name] for _,x in data_df.iterrows() if not x['malignant']])
    return (malignant_average+benign_average)/2

def get_stdev_threshold(param_name):
    mal_stdevs = []
    ben_stdevs = []
    for _,row in data_df.iterrows():
        nuclei_values = [row[param_name+i] for i in nuclei_index]
        if row['malignant']:
            mal_stdevs.append(stdev(nuclei_values))
        else:
            ben_stdevs.append(stdev(nuclei_values))
    return (mean(mal_stdevs)+mean(ben_stdevs))/2

def predict(df):
    pass

params = ['radius', 'area', 'smoothness', 'concavity', 'compactness', 'concave points', 'symmetry', 'fractal dimension']
stdev_params = ['texture']

