import pandas as pd
from math import isnan


class Evaluation:
    def __init__(self, probabilities={}):
        self.probabilities = probabilities

    def set_probabilities(self, probabilities, path='evaluations.csv'):
        self.probabilities = probabilities
        self.write_to_csv(path)

    def get_probabilities(self, path='evaluations.csv'):
        self.read_from_csv(path)
        return self.probabilities

    def write_to_csv(self, path):
        df = pd.DataFrame(self.probabilities)

        df = df.rename(columns={'': 'NULL_'})
        df = df.rename(index={'': 'NULL_'})

        df.to_csv(path)

    def read_from_csv(self, path):
        df = pd.read_csv(path)

        df = df.set_index(df.columns[0])
        df = df.rename(columns={'NULL_': ''})
        df = df.rename(index={'NULL_': ''})

        dic = df.to_dict()

        probabilities = {n_word: {
            f_word: dic[n_word][f_word] for
            f_word in dic[n_word].keys() if not isnan(dic[n_word][f_word])} for
            n_word in dic.keys()}

        self.probabilities = probabilities
