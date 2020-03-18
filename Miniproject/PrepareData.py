import pandas as pd
import sys


def prepare_data(path, entries_number, output_filename):
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

    df = df.sample(frac=1, random_state=21).reset_index(drop=True)
    df.head(entries_number).to_csv(output_filename)


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    output_filename = sys.argv[2] if len(sys.argv) > 2 else 'stackoverflow.csv'
    prepare_data('stacksample', n, output_filename)
