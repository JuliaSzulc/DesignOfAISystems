import pandas as pd


def prepare_data(path, entries_number):
    questions_path = path + '/Questions.csv'
    tags_path = path + '/Tags.csv'
    df = pd.read_csv(questions_path, encoding="ISO-8859-1")
    df = df.drop(columns=['Body'])

    tags = pd.read_csv(tags_path, encoding="ISO-8859-1", dtype={'Tag': str})
    tags['Tag'] = tags['Tag'].astype(str)
    grouped_tags = tags.groupby("Id")['Tag'].apply(lambda tags: ' '.join(tags))
    grouped_tags.reset_index()

    grouped_tags_final = pd.DataFrame({'Id': grouped_tags.index, 'Tags': grouped_tags.values})

    df = df.merge(grouped_tags_final, on='Id')

    df.head(entries_number).to_csv("stackoverflow.csv")


if __name__ == '__main__':
    prepare_data('stacksample', 10000)
