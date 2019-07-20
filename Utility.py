# -*- SIMILARITY -*-
def cos_sim(a, b):
    """
    Return the cosine similarity between vector a and b.
    """
    numerator, sosA, sosB = 0, 0, 0 #sum of squares for denom
    for i in movies: #replace movies
        numerator += (ratingai * ratingbi)
        sosA += ratingai * ratingai
        sosB += ratingbi * ratingbi
    denom = sqrt(sosA * sosB)  #make sure denom won't be 0!
    return numerator / denom


def adj_cos_sim(a, b, avg_a, avg_b):
    """
    Return the adjusted cosine similarity between vector a and b.
    """
    adj_a, adj_b = [], []
    for val in a: #replace a, not necessarily a vector if we do OOP
        adj_a.append(val - avg_a) #negative res
    for val in b:
        adj_b.append(val - avg_b)
    return cos_sim(adj_a, adj_b)  #is this slower than if I wrote it out/expanded it?



# -*- DATA RETRIEVAL -*-
def listGenres(movieId):
    """
    Takes in a movie's ID and returns a list of strings representing the genres
    pertaining to the movie.
    Access the movies dataframe to convert the large concatenated string
    delimited by '|'.
    """
    genres = movies.at[movieId, 'genres']  #change movies to whatever variable name the movies df has
    genres = genres.split('|')
    return genres



# -*- MODEL EVALUATION -*-
def mae(predicted, actual):
    """
    Takes in a list of predicted ratings and a list of actual ratings for a set
    of movies and computes the mean absolute error of our predictions.
    """
    #maybe make some assertions, assume have same length & in right order
    interm_total = 0
    for i in range(len(predicted)):
          interm_total += abs(predicted[i] - actual[i])
    return interm_total / len(predicted)


def rmse(predicted, actual):
    """
    Takes in a list of predicted ratings and a list of actual ratings for a set
    of movies and computes the root mean square error of our predictions.
    """
    #maybe make some assertions, assume have same length & in right order
    interm_total = 0
    for i in range(len(predicted)):
          interm_total += (predicted[i] - actual[i]) ** 2
    return sqrt(interm_total / len(predicted))
