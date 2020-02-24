import pickle
import pandas as pd
from statistics import mean, stdev
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

nuclei_index = ['_0', '_1', '_2']
params = ['perimeter', 'area', 'concave points',
          'concavity', 'radius', 'compactness']
stdev_params = ['texture']
thresholds = {}


def define_rule(param):
    return lambda x: x[param] >= thresholds[param]


def define_stdev_rule(param):
    return lambda x: stdev(x[param + i] for i in nuclei_index) >= thresholds[param]


def get_threshold(param_name, data):
    malignant_average = mean(
        [x[param_name] for _, x in data.iterrows() if x['malignant']])
    benign_average = mean(
        [x[param_name] for _, x in data.iterrows() if not x['malignant']])
    return (malignant_average + benign_average) / 2


def get_stdev_threshold(param_name, data):
    mal_stdevs = []
    ben_stdevs = []
    for _, row in data.iterrows():
        nuclei_values = [row[param_name + i] for i in nuclei_index]
        if row['malignant']:
            mal_stdevs.append(stdev(nuclei_values))
        else:
            ben_stdevs.append(stdev(nuclei_values))
    return (mean(mal_stdevs) + mean(ben_stdevs)) / 2


def predict(X):
    Y_pred = []
    for _, x in X.iterrows():
        Y_pred.append(predict_single_entry(x))
    return Y_pred


def fit(X, Y):
    df = X.copy()
    df['malignant'] = Y
    for param in params:
        for i in nuclei_index:
            param_name = param + i
            thresholds[param_name] = get_threshold(param_name, df)
    for param in stdev_params:
        thresholds[param] = get_stdev_threshold(param, df)


def predict_single_entry(x):
    for param in params:
        for i in nuclei_index:
            if define_rule(param + i)(x):
                return 1
    for stdev_param in stdev_params:
        if define_stdev_rule(stdev_param)(x):
            return 1
    return 0


def classify(df):
    Y = df['malignant']
    X = df.drop('malignant', 1)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    fit(X_train, Y_train)
    Y_pred = predict(X_test)
    print(accuracy_score(Y_test, Y_pred))
