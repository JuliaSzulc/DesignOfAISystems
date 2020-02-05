from Utils.py import get_euclidan_distances

class KNNClassifier:

    def __init__(self, K):
        self.data = None
        self.labels = None
        self.K = K

    def fit(self, X,Y):
        self.data = X
        self.labels = Y

    def predict(self, X):
        for _,row in X.iterrows():
           self.predict_label(row)

    def predict_label(self,row):
        distances = get_euclidan_distances(self.data,row)
        distances = sorted(distances, key=distances.get)
        indexes = distances[:self.K]
        return self.evaluate_most_common_label(indexes)

    def evaluate_most_common_label(self, indexes):
        count_ones = sum(self.labels[i] for i in indexes)
        if count_ones > self.K/2:
            return 1
        else:
            return 0


    def score(self):
        pass
