from DataProcessor import *

if __name__ == '__main__':
    dp = DataProcessor()
    dp.prepare_data()
    x1, x2, y1, y2 = dp.get_data_splits()
    print(x2.head())
