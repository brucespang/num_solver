import unittest
import numpy as np

from num_solver import *

DELTA = 0.01

class TestNUM(unittest.TestCase):
    def test_equal_shared_link(self):
        utility = lambda x: np.sum(np.ma.log(x))
        R = np.array([[1., 1.]])
        capacity = np.array([10.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(5. - res[0]) < DELTA)
        self.assertTrue(abs(5. - res[1]) < DELTA)

    def test_unequal_shared_link(self):
        w = np.array([1., 2.])
        utility = lambda x: np.dot(w, np.ma.log(x))
        R = np.array([[1., 1.]])
        capacity = np.array([9.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(3. - res[0]) < DELTA)
        self.assertTrue(abs(6. - res[1]) < DELTA)

    def test_unshared_link(self):
        w = np.array([1., 2.])
        utility = lambda x: np.dot(w, np.ma.log(x))
        R = np.array([[1., 0.], [0., 1.]])
        capacity = np.array([10., 10.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(10. - res[0]) < DELTA)
        self.assertTrue(abs(10. - res[1]) < DELTA)

    def test_zero_capacity(self):
        w = np.array([1., 2.])
        utility = lambda x: np.dot(w, np.ma.log(x))
        R = np.array([[1., 0.], [0., 1.]])
        capacity = np.array([10., 0.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(10. - res[0]) < DELTA)
        self.assertTrue(abs(0. - res[1]) < DELTA)

    def test_many_resources(self):
        R = np.matrix([[1., 0., 0.],
                       [0., 1., 0.],
                       [0., 0., 1.],
                       [1., 1., 0.],
                       [0., 1., 1.],
                       [1., 0., 1.],
                       [1., 1., 1.]])
        capacity = np.array([30., 5., 30., 20., 10., 10., 20.])
        utility = lambda x: np.sum(np.ma.log(x))

        solve_num_problem(utility, R, capacity)


if __name__ == '__main__':
    unittest.main()
