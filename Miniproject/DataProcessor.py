import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split


class DataProcessor:
    def __init__(self, path="stackoverflow.csv", test_size=0.25):
        self.path = path
        self.data = None
        self.unique_tags = []
        self.test_size = test_size

        self.prepare_data()

    def prepare_data(self):
        self.data = pd.read_csv(self.path, encoding="ISO-8859-1")
        self.data = self.data.filter(['Title', 'Tags'])
        self.prepare_tags()

    def prepare_tags(self):
        self.data['Tags'] = self.data['Tags'].apply(
            lambda question_tags: question_tags.split())
        self.unique_tags = self.get_filtered_tags()
        self.data['Tags'] = self.data['Tags'].apply(
            lambda question_tags: self.filter_unique_tags(question_tags))
        self.filter_entries_by_tags()

    def get_filtered_tags(self):
        all_tags = [tag for tags in self.data['Tags'].values for tag in tags]
        filtered_tags = self.filter_tags(all_tags)
        return filtered_tags

    def filter_tags(self, all_tags):
        filtered_tags = []
        tags_counter = Counter(all_tags)
        for tag in tags_counter.keys():
            if tags_counter[tag] > 1:
                filtered_tags.append(tag)
        return filtered_tags

    def filter_unique_tags(self, tags):
        filtered_tags = [tag for tag in tags if tag in self.unique_tags]
        return filtered_tags

    def filter_entries_by_tags(self):
        is_entry_valid = [any([tag in self.unique_tags for tag in tags])
                          for tags in self.data['Tags']]
        self.data = self.data[is_entry_valid]

    def get_data_splits(self):
        x_train, x_test, y_train, y_test = \
            train_test_split(self.data['Title'], self.data['Tags'],
                             test_size=self.test_size, random_state=42)
        return x_train, x_test, y_train, y_test
