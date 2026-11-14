import unittest
import numpy as np
from semantic_search import nearest_movies


class NearestMoviesTests(unittest.TestCase):
    def test_ranks_by_squared_euclidean_distance(self):
        vectors = np.array([[0.0, 0.0], [2.0, 0.0], [1.0, 0.0]], dtype=np.float32)
        self.assertEqual(nearest_movies(vectors, np.array([1.1, 0.0]), limit=2).tolist(), [2, 1])

    def test_returns_only_available_movies(self):
        vectors = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
        self.assertEqual(len(nearest_movies(vectors, np.array([1.0, 0.0]), limit=5)), 2)


if __name__ == '__main__':
    unittest.main()
