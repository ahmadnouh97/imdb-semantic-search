import numpy as np


def nearest_movies(vectors, query_vector, limit=5):
    """Return row indices ordered by Chroma's default squared L2 distance."""
    distances = np.sum((vectors - query_vector) ** 2, axis=1)
    return np.argsort(distances, kind="stable")[:limit]
