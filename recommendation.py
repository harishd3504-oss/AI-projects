import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave', 'Dave'],
    'Movie': ['Titanic', 'Avatar', 'Titanic', 'Inception', 'Avatar', 'Inception', 'Titanic', 'Avatar'],
    'Rating': [5, 3, 4, 5, 2, 4, 5, 3]
}

df = pd.DataFrame(data)
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def recommend_movies(user, top_n=2):
    similar_users = user_similarity_df[user].sort_values(ascending=False).drop(user)
    recommended_movies = pd.Series(dtype=float)
    for other_user, similarity_score in similar_users.items():
        other_user_ratings = user_movie_matrix.loc[other_user]
        unrated_movies = other_user_ratings[user_movie_matrix.loc[user] == 0]
        recommended_movies = recommended_movies.append(unrated_movies * similarity_score)
    recommended_movies = recommended_movies.groupby(recommended_movies.index).sum()
    recommended_movies = recommended_movies.sort_values(ascending=False)
    return recommended_movies.head(top_n)

print(recommend_movies('Alice'))