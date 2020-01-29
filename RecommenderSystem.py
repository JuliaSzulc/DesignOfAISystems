import pandas as pd

REVIEWS_PATH = 'data/user_reviews.csv'
GENRES_PATH = 'data/movie_genres.csv'

CORR_PATH = 'data/movie_corr.csv'

reviews_df = pd.read_csv(REVIEWS_PATH)
reviews_df = reviews_df.drop(reviews_df.columns[0], axis=1)

genres_df = pd.read_csv(GENRES_PATH)

titles = list(reviews_df)[1:]
corr_df = pd.DataFrame()
i = 0

for title in titles:
    movie_corr = reviews_df.corrwith(reviews_df[title])
    corr_df = pd.concat([corr_df, movie_corr], axis=1, sort=False)
    i += 1
    print(i)

corr_df.columns = titles
corr_df.to_csv(CORR_PATH)
print(corr_df)
