import pandas as pd
from collections import Counter

def prepare_data(path="stackoverflow.csv"):
    df = pd.read_csv(path, encoding="ISO-8859-1")
    df.drop(columns=['Id', 'Unnamed: 0','OwnerUserId', 'CreationDate', 'ClosedDate', 'Body', 'Score'], inplace=True)
    df = prepare_tags(df)


    #Split data in to testing and training (vill ha med all tags någon gång i training)


def prepare_tags(df):
    df['Tags'] = df['Tags'].apply(lambda question_tags: question_tags.split())
    tags = get_unique_tags(df)
    df['Tags'] = df['Tags'].apply(lambda question_tags: filter_unique_tags(question_tags, tags))
    df['Tags'] = df['Tags'].apply(lambda question_tags: None if len(question_tags) == 0 else question_tags)
    df.dropna(inplace=True)
    return df

def get_unique_tags(df):
    all_tags = [tag for tags in df['Tags'].values for tag in tags]
    tags = filter_tags(all_tags)
    return tags

def filter_tags(all_tags):
    filtered_tags = []
    tags_counter = Counter(all_tags)
    for tag in tags_counter.keys():
        if tags_counter[tag] > 1:
            filtered_tags.append(tag)
    return filtered_tags

def filter_unique_tags(tags, unique_tags):
    filtered_tags = []
    for tag in tags:
        if tag in unique_tags:
            filtered_tags.append(tag)
    return filtered_tags


prepare_data()