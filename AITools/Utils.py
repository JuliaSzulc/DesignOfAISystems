import math
import pandas as pd

def calculate_euclidian_distance(row1, row2):

    sum=0
    for label, content in row1.items():
        sum += (content-row2[label])**2

    return math.sqrt(sum)

def get_euclidan_distances(df, newrow):

    distances = {}
    for index,row in df.iterrows():
        distances[index] = calculate_euclidian_distance(row,newrow)

    return distances


def prepare_data_and_labels(df1, df2=pd. DataFrame()):
    if not df2.empty:
        df1 = df1.append(df2, ignore_index=True)

    Y = df1['PM_HIGH']
    X = df1.drop(columns='PM_HIGH')

    return X, Y
