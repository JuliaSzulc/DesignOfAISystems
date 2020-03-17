import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split


class DataProcessor:
    def __init__(self, path="stackoverflow.csv"):
        self.path = path
        self.data = None
        self.unique_tags = []

    def prepare_data(self):
        self.df = pd.read_csv(self.path, encoding="ISO-8859-1")
        self.df = self.df.filter(['Title', 'Tags'])
        self.prepare_tags()

    def prepare_tags(self):
        self.df['Tags'] = self.df['Tags'].apply(
            lambda question_tags: question_tags.split())
        valid_tags = self.get_filtered_tags()
        self.df['Tags'] = self.df['Tags'].apply(
            lambda question_tags: self.filter_unique_tags(question_tags, valid_tags))
        self.filter_entries_by_tags(valid_tags)

    def get_filtered_tags(self):
        all_tags = [tag for tags in self.df['Tags'].values for tag in tags]
        filtered_tags = self.filter_tags(all_tags)
        return filtered_tags

    def filter_tags(self, all_tags):
        filtered_tags = []
        tags_counter = Counter(all_tags)
        for tag in tags_counter.keys():
            if tags_counter[tag] > 1:
                filtered_tags.append(tag)
        return filtered_tags

    def filter_unique_tags(self, tags, valid_tags):
        filtered_tags = [tag for tag in tags if tag in valid_tags]
        return filtered_tags

    def filter_entries_by_tags(self, valid_tags):
        is_entry_valid = [any([tag in valid_tags for tag in tags])
                          for tags in self.df['Tags']]
        self.df = self.df[is_entry_valid]

    def get_data_splits(self):
        x_train, x_test, y_train, y_test = \
            train_test_split(self.df['Title'], self.df['Tags'], random_state=42)
        return x_train, x_test, y_train, y_test
