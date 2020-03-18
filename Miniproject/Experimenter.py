from Model import *

class Experimenter:

    def __init__(self, unique_tags, X_train, X_test, Y_train, Y_test):
        self.unique_tags = unique_tags
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test

    def run_all_experiments(self):
        print("Score without ngrams or stopwords: {}".format(self.run_experiment(ngram=False, stopwords=False)))

        print("Score using ngrams only: {}".format(self.run_experiment(ngram=True, stopwords=False)))

        print("Score using stopwords only: {}".format(self.run_experiment(ngram=False, stopwords=True)))

        print("Score using both ngrams and stopwords: {}".format(self.run_experiment(ngram=True, stopwords=True)))

    def run_experiment(self,ngram=False,stopwords=False):
        clf = Model(ngrams=ngram, stopwords=stopwords, unique_tags=self.unique_tags)
        clf.fit(self.X_train, self.Y_train)
        y = clf.predict(self.X_test)
        return clf.score(y, self.Y_test)