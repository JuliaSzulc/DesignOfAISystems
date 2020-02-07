import math
import pandas as pd


def calculate_euclidean_distance(row1, row2):
    sum_of_squares = 0
    for label, content in row1.items():
        sum_of_squares += (content - row2[label]) ** 2

    return math.sqrt(sum_of_squares)


def get_euclidean_distances(df, new_row):
    distances = {}
    for index, row in df.iterrows():
        distances[index] = calculate_euclidean_distance(row, new_row)

    return distances


def prepare_data_and_labels(df1, df2=pd.DataFrame()):
    if not df2.empty:
        df1 = df1.append(df2, ignore_index=True)

    Y = df1['PM_HIGH']
    X = df1.drop(columns='PM_HIGH')

    return X, Y


