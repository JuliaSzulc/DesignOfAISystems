import sys

from DataProcessor import *
from Experimenter import *

if __name__ == '__main__':
    data_file = sys.argv[1] if len(sys.argv) > 1 else 'stackoverflow.csv'
    optimal_features = 25000

    dp = DataProcessor(path=data_file, test_size=0.2)
    x_train, x_test, y_train, y_test = dp.get_data_splits()

    exp = Experimenter(dp.unique_tags, x_train, x_test, y_train, y_test)
    # exp.run_all_experiments(max_features=optimal_features)
    exp.run_experiment(stopwords=True,
                       bigrams=False,
                       max_features=optimal_features,
                       save_model=False)
