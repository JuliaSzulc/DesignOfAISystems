import math

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
