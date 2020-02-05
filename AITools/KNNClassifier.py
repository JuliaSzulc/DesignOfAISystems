from Utils import get_euclidan_distances

class KNNClassifier:

    def __init__(self, K):
        self.data = None
        self.labels = None
        self.K = K

    def fit(self, X,Y):
        self.data = X
        self.labels = Y

    def predict(self, X):
        predictions = []
        for _,row in X.iterrows():
           predictions.append(self.predict_label(row))

        return predictions

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

    def score(self, Y_predicted, Y_real):
        if len(Y_predicted)!=len(Y_real):
            print("Different sizes on predicted and real.")
            return -1
        length = len(Y_predicted)
        correct_count = sum(1 for i in range(0,length) if Y_predicted[i]==Y_real[i])
        return correct_count/length
