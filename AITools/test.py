import pandas as pd

from Utils import prepare_data_and_labels
from KNNClassifier import *

BEIJING_PATH = 'data/Beijing_labeled.csv'
CHENGDU_PATH = 'data/Chengdu_labeled.csv'
GUANGZHOU_PATH = 'data/Guangzhou_labeled.csv'
SHANGHAI_PATH = 'data/Shanghai_labeled.csv'
SHENYANG_PATH = 'data/Shenyang_labeled.csv'


def main():
    df_beijing = pd.read_csv(BEIJING_PATH)
    df_shenyang = pd.read_csv(SHENYANG_PATH)

    X_train, Y_train = prepare_data_and_labels(df_beijing, df_shenyang)

    print("fitting...")

    clf = KNNClassifier(K=5)
    clf.fit(X_train, Y_train)

    # print("validating")
    # cv_score = cross_val_score(clf, X_train, Y_train)
    # print("cv score:", cv_score)

    print("predicting...")
    df_guangzhou = pd.read_csv(GUANGZHOU_PATH)
    df_shanghai = pd.read_csv(SHANGHAI_PATH)

    df_guangzhou = df_guangzhou.head(20)

    X_test, Y_test = prepare_data_and_labels(df_guangzhou)

    Y_pred = clf.predict(X_test)

    print("scoring...")
    score = clf.score(Y_pred, Y_test)
    print(score)

main()
