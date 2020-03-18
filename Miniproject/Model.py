from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.pipeline import make_pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression

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
        self.classifier = OneVsRestClassifier(LogisticRegression())

        self.pipeline = make_pipeline(self.vectorizer,
                                      self.classifier)

    def fit(self, x, y):
        print('Fitting...')
        encoded_y = self.label_binarizer.fit_transform(y)

        #  multiclass.py prints warning if all the entries have the same label value
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)
            self.pipeline.fit(x, encoded_y)

    def predict(self, x):
        print('Predicting...')
        y_predicted = self.pipeline.predict(x)
        return y_predicted

    def score(self, y_predicted, y_real):
        print('Scoring...')
        decoded_y = self.label_binarizer.inverse_transform(y_predicted)
        correct_predictions = 0

        for pred_tags, real_tags in zip(decoded_y, y_real):
            n = len(real_tags)
            first_n_pred = pred_tags[:n]

            if any([tag in real_tags for tag in first_n_pred]):
                correct_predictions += 1

        score = correct_predictions / len(y_predicted)

        return score
