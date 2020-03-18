import sys

from DataProcessor import *
from Experimenter import *

if __name__ == '__main__':
    data_file = sys.argv[1] if len(sys.argv) > 1 else 'stackoverflow.csv'

    dp = DataProcessor(path=data_file, test_size=0.2)
    x_train, x_test, y_train, y_test = dp.get_data_splits()

    exp = Experimenter(dp.unique_tags, x_train, x_test, y_train, y_test)
    # exp.run_all_experiments()
    exp.run_experiment(stopwords=True, bigrams=True, validation=True)
