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
    Return the cosine similarity between vector a and b.
    (Cosine similarity )
    """
    adj_a, adj_b = [], []
    for val in a: #replace a, not necessarily a vector if we do OOP
        adj_a.append(val - avg_a) #negative res
    for val in b:
        adj_b.append(val - avg_b)
    return cos_sim(adj_a, adj_b)  #is this slower than if I wrote it out/expanded it?



def get_neighbors(target, k):
    """
    Return a list of the k closest neighbors of target user,
    where the closeness is based on cosine similarity between
    the user vectors.
    """
    similarities = []
    for i in users: #replace users
        similarities.append([i, cos_sim(target, i)])
    similarities.sort(key=lambda pair: -pair[1]) #negate to have larger sim scores come first
    k_neighbors = []
    for i in range(k):
        k_neighbors.append(simiarities[i][0])
    return k_neighbors
