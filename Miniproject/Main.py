from DataProcessor import *
from Model import *
from Experimenter import *

if __name__ == '__main__':
    dp = DataProcessor()
    x1, x2, y1, y2 = dp.get_data_splits()

    clf = Model(unique_tags=dp.unique_tags)
    clf.fit(x1, y1)
    y = clf.predict(x2)
    score = clf.score(y, y2)
    print(score)

    # exp = Experimenter(dp.unique_tags, x1, x2, y1, y2)
    # exp.run_all_experiments()


