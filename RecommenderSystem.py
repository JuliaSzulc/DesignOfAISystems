import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

REVIEWS_PATH = 'data/user_reviews.csv'
GENRES_PATH = 'data/movie_genres.csv'

CORR_PATH = 'data/movie_corr.csv'

reviews_df = pd.read_csv(REVIEWS_PATH)
reviews_df = reviews_df.drop(reviews_df.columns[0], axis=1)

genres_df = pd.read_csv(GENRES_PATH)

titles = list(reviews_df)[1:]
# corr_df = pd.DataFrame()
# i = 0
#
# for title in titles:
#     movie_corr = reviews_df.corrwith(reviews_df[title])
#     corr_df = pd.concat([corr_df, movie_corr], axis=1, sort=False)
#     i += 1
#     print(i)
#
# corr_df.columns = titles
# corr_df.to_csv(CORR_PATH)
# print(corr_df)

ratings = reviews_df.drop('User', axis=1).to_numpy()
mean_user_ratings = np.mean(ratings, axis=1)
normalized_ratings = ratings - mean_user_ratings.reshape(-1, 1)

u, s, vt = svds(normalized_ratings, k = 10)

predicted_ratings = np.dot(np.dot(u, np.diag(s)), vt) + mean_user_ratings.reshape(-1, 1)
predictions_df = pd.DataFrame(predicted_ratings, columns = titles)
print(predictions_df)
