from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.pipeline import make_pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
import numpy as np

import warnings


class Model:
    def __init__(self, stopwords=False, ngrams=False, max_features=None,
                 unique_tags=None):
        ngram_range = (1, 2) if ngrams else (1, 1)
        stopwords = 'english' if stopwords else None

        self.label_binarizer = MultiLabelBinarizer(classes=unique_tags)
        self.vectorizer = CountVectorizer(stop_words=stopwords,
                                          ngram_range=ngram_range,
                                          max_features=max_features)
        self.classifier = OneVsRestClassifier(MultinomialNB())

        self.pipeline = make_pipeline(self.vectorizer,
                                      self.classifier)

    def fit(self, x, y):
        print('Fitting...')
        encoded_y = self.label_binarizer.fit_transform(y)

        # multiclass.py prints warning if all the entries have the same label value
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            self.pipeline.fit(x, encoded_y)

    # For each entry returns a vector of probabilities
    def predict(self, x):
        print('Predicting...')
        x_transformed = self.vectorizer.transform(x)
        y_predicted = self.classifier.predict_proba(x_transformed)
        return y_predicted

    def score(self, y_probabilities, y_real):
        print('Scoring...')
        correct_predictions = 0

        for probabilities, real_tags in zip(y_probabilities, y_real):
            n = len(real_tags)
            top_n_indexes = np.argpartition(probabilities, -n)[-n:]
            predicted_tags = self.label_binarizer.classes_[top_n_indexes]

            if any([tag in predicted_tags for tag in real_tags]):
                correct_predictions += 1

        score = correct_predictions / len(y_probabilities)

        return score
