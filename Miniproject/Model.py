from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
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
        self.classifier = OneVsRestClassifier(LogisticRegression(),
                                              n_jobs=-1)

    def fit(self, x, y):
        print('Fitting...', end='\r')
        encoded_y = self.label_binarizer.fit_transform(y)
        vectorized_x = self.vectorizer.fit_transform(x, encoded_y)

        # multiclass.py prints warning if all the entries have the same label value
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            self.classifier.fit(vectorized_x, encoded_y)

    def validate(self, x, y):
        encoded_y = self.label_binarizer.fit_transform(y)
        vectorized_x = self.vectorizer.fit_transform(x, encoded_y)

        # multiclass.py prints warning if all the entries have the same label value
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            cv_scores = cross_val_score(self.classifier, vectorized_x, encoded_y, cv=5)

        return cv_scores

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
            top_n_indexes = np.argpartition(probabilities, -tags_n)[-tags_n:]
            predicted_tags = self.label_binarizer.classes_[top_n_indexes]
            required_n = ceil(tags_n / 2)

            if self.check_if_at_least_n_are_common(required_n, predicted_tags,
                                                   real_tags):
                correct_predictions += 1

        score = correct_predictions / len(y_probabilities)

        return score

    def check_if_at_least_n_are_common(self, n, predicted_tags, real_tags):
        is_common = [tag in predicted_tags for tag in real_tags]
        are_at_least_n = all(map(any, repeat(iter(is_common), n)))

        return are_at_least_n
