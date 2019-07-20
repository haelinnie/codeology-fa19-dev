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
