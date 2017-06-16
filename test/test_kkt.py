import unittest
import numpy as np
import random

from num_solver import *
from num_solver.utility_functions import *

DELTA = 1e-10

class TestNUM(unittest.TestCase):
    def test_equal_shared_link(self):
        random.seed(0)
        np.random.seed(0)
        R,c = networks.generate_full_rank_topology(12)
        w = np.array([np.random.random() + 1 for _ in range(num_flows(R))])

        x = solve(weighted_log(w), R, c, tol=1e-15)
        price = np.linalg.solve(R.T, w/x)

        self.assertTrue(abs(0. - np.dot(price, np.dot(R,x) - c)) < DELTA)

if __name__ == '__main__':
    unittest.main()
