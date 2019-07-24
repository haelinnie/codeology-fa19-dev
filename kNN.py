import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

class kNN:
    def __init__(self, path, mov_file, ratings_file):
        self.mov_path = path + mov_file
        self.ratings_path = path + ratings_file

    def prep(self):
        movies = pd.read_csv(self.mov_path)
        ratings = pd.read_csv(self.ratings_path)
        movies = movies.drop('genres', axis=1)
        ratings = ratings.drop('timestamp', axis=1)

        ratings_popular = handle_sparcity()

    def handle_sparcity():
        ratings_popular = ratings.groupby('movieId').filter(lambda x: len(x) >= 100)
        user_popular = ratings_popular.groupby('userId').filter(lambda x: len(x) >= 100)
        return user_popular
