"""
Design of AI Systems
Assignment no. 3
Sarah Lindau, Julia Szulc
Chalmers University of Technology, 2020
"""

import pandas as pd
from sklearn.model_selection import KFold

from Utils import prepare_data_and_labels
from KNNClassifier import *

BEIJING_PATH = 'data/Beijing_labeled.csv'
CHENGDU_PATH = 'data/Chengdu_labeled.csv'
GUANGZHOU_PATH = 'data/Guangzhou_labeled.csv'
SHANGHAI_PATH = 'data/Shanghai_labeled.csv'
SHENYANG_PATH = 'data/Shenyang_labeled.csv'


def validate(clf, X, Y, n_splits=5):
    print("Validation phase:")

    kf = KFold(n_splits=n_splits, shuffle=True)
    total_score = 0

    for i, (train_index, test_index) in enumerate(kf.split(X)):
        print("validation %d/%d" % (i, n_splits))

        X_train, X_validate = X.iloc[train_index], X.iloc[test_index]
        Y_train, Y_validate = Y.iloc[train_index], Y.iloc[test_index]

        clf.fit(X_train, Y_train)
        Y_pred = clf.predict(X_validate)

        total_score += clf.score(Y_pred, Y_validate)

    total_score /= n_splits
    print("accuracy: %f\n" % total_score)


def test(clf, X_test, Y_test):
    print("Testing phase:")

    Y_pred = clf.predict(X_test)

    score = clf.score(Y_pred, Y_test)
    print("accuracy: %f\n" % score)


def main():
    df_beijing = pd.read_csv(BEIJING_PATH)
    df_shenyang = pd.read_csv(SHENYANG_PATH)
    X, Y = prepare_data_and_labels(df_beijing, df_shenyang)

    clf = KNNClassifier(K=5)
    validate(clf, X, Y)

    print("GUANGZHOU")
    df_guangzhou = pd.read_csv(GUANGZHOU_PATH)
    X_test, Y_test = prepare_data_and_labels(df_guangzhou)
    test(clf, X_test, Y_test)

    print("SHANGHAI")
    df_shanghai = pd.read_csv(SHANGHAI_PATH)
    X_test, Y_test = prepare_data_and_labels(df_shanghai)
    test(clf, X_test, Y_test)


main()
