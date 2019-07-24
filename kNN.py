import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

class kNN:
    def __init__(self, path, mov_file, ratings_file):
        """
        Initialize an instance of the kNN recommender.
        Pass in the general path, the name of the movies file, the name of the
        ratings file as three strings.
        """
        self.mov_path = path + mov_file
        self.ratings_path = path + ratings_file



    def prepared_data(self):
        """
        Clean the ratings data by filtering out unpopular movies and inactive
        users.
        Save the id: title/title: id mappings constructed upon the filtered set
        of movies.
        Return a sparse csr matrix constructed upon the filtered ratings data
        """
        movies = pd.read_csv(self.mov_path)
        ratings = pd.read_csv(self.ratings_path)
        movies = movies.drop('genres', axis=1)
        ratings = ratings.drop('timestamp', axis=1)

        ratings_active_usrs = self.handle_sparcity(ratings, 'userId', 100)
        ratings_popular_movs = self.handle_sparcity(ratings_active_users, 'movieId', 100)

        mov_usr_table = ratings_popular.pivot(index='movieId', columns='userId', values='rating').fillna(0)
        movie_usr_csr = csr_matrix(mov_user_table)

        title_ind_map = {movie: i
           for i, movie
           in enumerate(list(movies.set_index('movieId').loc[mov_user_table.index].title))}
        ind_title_map = {i: movie for movie, i in mov_ind_map.items()}
        self.mappings = [title_ind_map, ind_title_map]

        return movie_usr_csr



    def handle_sparcity(self, df, group, threshold):
        """
        Helper function to filter out rows of a dataframe given a column
        to group by and a minimum count threshold to be met.
        """
        return df.groupby(group).filter(lambda x: len(x) >= threshold)



    def title_to_id(self, title):
        """
        Return the id of a movie given its title.
        """
        return self.mappings[0][title]



    def id_to_title(self, id):
        """
        Return the title of a movie given its id.
        """
        return self.mappings[1][id]
