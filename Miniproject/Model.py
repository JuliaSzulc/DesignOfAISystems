from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import SGDClassifier
import numpy as np
from math import ceil
from itertools import repeat
import warnings


class Model:
    def __init__(self, stopwords=False, bigrams=False, max_features=None,
                 unique_tags=None):
        ngram_range = (1, 2) if bigrams else (1, 1)
        stopwords = 'english' if stopwords else None

        self.label_binarizer = MultiLabelBinarizer(classes=unique_tags)
        self.vectorizer = CountVectorizer(stop_words=stopwords,
                                          ngram_range=ngram_range,
                                          max_features=max_features)
        self.classifier = OneVsRestClassifier(SGDClassifier(loss='log'))

    def fit(self, x, y):
        print('Fitting...', end='\r')
        encoded_y = self.label_binarizer.fit_transform(y)
        vectorized_x = self.vectorizer.fit_transform(x, encoded_y)

        # multiclass.py prints warning if all the entries have the same label value
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            self.classifier.fit(vectorized_x, encoded_y)

    # For each entry returns a vector of probabilities
    def predict(self, x):
        print('Predicting...', end='\r')
        x_transformed = self.vectorizer.transform(x)
        y_predicted = self.classifier.predict_proba(x_transformed)
        return y_predicted

    def score(self, y_probabilities, y_real):
        print('Scoring...', end='\r')
        correct_predictions = 0

        for probabilities, real_tags in zip(y_probabilities, y_real):
            tags_n = len(real_tags)
            predicted_tags = self.evaluate_top_n_tags(tags_n, probabilities)

            required_n = ceil(tags_n / 2)
            if self.check_if_at_least_n_are_common(required_n, predicted_tags,
                                                   real_tags):
                correct_predictions += 1

        score = correct_predictions / len(y_probabilities)

        return score

    def evaluate_top_n_tags(self, n, predicted_probabilities):
        top_n_indexes = np.argpartition(predicted_probabilities, -n)[-n:]
        predicted_tags = self.label_binarizer.classes_[top_n_indexes]
        return predicted_tags

    def check_if_at_least_n_are_common(self, n, predicted_tags, real_tags):
        is_common = [tag in predicted_tags for tag in real_tags]
        are_at_least_n = all(map(any, repeat(iter(is_common), n)))

        return are_at_least_n
