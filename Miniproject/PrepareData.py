import pandas as pd


df = pd.read_csv("stacksample/Questions.csv", encoding="ISO-8859-1")

tags = pd.read_csv("stacksample/Tags.csv", encoding="ISO-8859-1", dtype={'Tag': str})
tags['Tag'] = tags['Tag'].astype(str)
grouped_tags = tags.groupby("Id")['Tag'].apply(lambda tags: ' '.join(tags))
grouped_tags.reset_index()


grouped_tags_final = pd.DataFrame({'Id':grouped_tags.index, 'Tags':grouped_tags.values})

df = df.merge(grouped_tags_final, on='Id')


df.head(10000).to_csv("stackoverflow.csv")