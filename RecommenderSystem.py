import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds


REVIEWS_PATH = 'data/user_reviews.csv'
GENRES_PATH = 'data/movie_genres.csv'


def calculate_svds_scores(k=20):
    ratings = reviews_df.drop('User', axis=1).to_numpy()
    mean_user_ratings = np.mean(ratings, axis=1).reshape(-1, 1)
    normalized_ratings = ratings - mean_user_ratings

    u, s, vt = svds(normalized_ratings, k=k)

    predicted_ratings = np.dot(np.dot(u, np.diag(s)), vt) + mean_user_ratings
    predictions_df = pd.DataFrame(predicted_ratings, columns=titles)

    return predictions_df


def print_summary(user_name, predictions_df, movies_number=5):
    user_index = reviews_df[reviews_df['User'] == user_name].index[0]

    best = get_best_reviews_with_genres(user_index, movies_number)
    recommended = generate_recommendations_with_genres(
        user_index, predictions_df, movies_number)

    print("\nTop %d %s's movies:" % (movies_number, user_name))
    print(best)
    print("\nRecommendations:")
    print(recommended)


def generate_recommendations_with_genres(user_index, predictions_df, movies_number=5):
    user_prediction_scores = predictions_df.iloc[user_index]\
        .sort_values(ascending=False)
    user_recommendations = pd.DataFrame({
        'score': user_prediction_scores[:movies_number],
        'genres': ""})

    for title, _ in user_recommendations.iterrows():
        user_recommendations.at[title, 'genres'] = get_genres(title)

    user_recommendations = user_recommendations.drop(['score'], axis=1)

    return user_recommendations


def get_best_reviews_with_genres(user_index, movies_number=5):
    user_reviewed_movies = get_user_reviews(user_index)
    user_best_movies = pd.DataFrame({
        'rating': user_reviewed_movies[:movies_number],
        'genres': ""})

    for title, _ in user_best_movies.iterrows():
        user_best_movies.at[title, 'genres'] = get_genres(title)

    return user_best_movies


def get_user_reviews(user_index):
    user_movies = reviews_df.iloc[user_index][1:]
    user_reviewed_movies = user_movies[user_movies > 0].sort_values(ascending=False)

    return user_reviewed_movies


def get_genres(movie_title):
    movie = genres_df[genres_df['movie_title'] == movie_title]\
        .drop(['movie_title'], axis=1)
    movie = movie[movie == 1].dropna(axis=1)
    genres = movie.columns.to_list()

    return genres


reviews_df = pd.read_csv(REVIEWS_PATH)
reviews_df = reviews_df.drop(reviews_df.columns[0], axis=1)

genres_df = pd.read_csv(GENRES_PATH)
genres_df = genres_df.drop(genres_df.columns[0], axis=1)
genres_df.columns = genres_df.columns.str.replace('genre_', '')

titles = list(reviews_df)[1:]

predictions_df = calculate_svds_scores()

print_summary('Mary', predictions_df)
