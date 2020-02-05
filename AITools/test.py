import pandas as pd

BEIJING_PATH = 'data/Beijing_labeled.csv'
CHENGDU_PATH = 'data/Chengdu_labeled.csv'
GUANGZHOU_PATH = 'data/Guangzhou_labeled.csv'
SHANGHAI_PATH = 'data/Shanghai_labeled.csv'
SHENYANG_PATH = 'data/Shenyang_labeled.csv'

def main():
    df = pd.read_csv(BEIJING_PATH)
