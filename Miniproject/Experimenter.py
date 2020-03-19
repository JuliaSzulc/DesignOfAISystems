import pickle

from Model import *


class Experimenter:
    def __init__(self, unique_tags, x_train, x_test, y_train, y_test):
        self.unique_tags = unique_tags
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def run_all_experiments(self, max_features=None):
        self.run_experiment(bigrams=False,
                            stopwords=False,
                            max_features=max_features,
                            description='Basic case (no stopwords, unigrams)')

        self.run_experiment(bigrams=True,
                            stopwords=False,
                            max_features=max_features,
                            description='Bigrams only')

        self.run_experiment(bigrams=False,
                            stopwords=True,
                            max_features=max_features,
                            description='Stopwords only')

        self.run_experiment(bigrams=True,
                            stopwords=True,
                            max_features=max_features,
                            description='Bigrams & stopwords')

    def run_experiment(self, bigrams=False, stopwords=False, max_features=None,
                       description='', save_model=False):
        print(description)
        clf = Model(bigrams=bigrams, stopwords=stopwords,
                    max_features=max_features, unique_tags=self.unique_tags)

        clf.fit(self.x_train, self.y_train)
        y_predicted = clf.predict(self.x_test)
        score = clf.score(y_predicted, self.y_test)
        print('Accuracy: {0:.4f}\n'.format(score))

        if save_model:
            with open('model.pkl', 'wb') as f:
                pickle.dump(clf, f)
