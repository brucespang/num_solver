import unittest
import numpy as np

from num_solver import *

DELTA = 0.01

class TestNUM(unittest.TestCase):
    def test_equal_shared_link(self):
        utility = proportionally_fair()
        R = np.array([[1., 1.]])
        capacity = np.array([10.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(5. - res[0]) < DELTA)
        self.assertTrue(abs(5. - res[1]) < DELTA)

    def test_solve_alias(self):
        utility = proportionally_fair()
        R = np.array([[1., 1.]])
        capacity = np.array([10.])

        res = solve(utility, R, capacity, tol=1e-5)
        self.assertTrue(abs(5. - res[0]) < DELTA)
        self.assertTrue(abs(5. - res[1]) < DELTA)

    def test_unequal_shared_link(self):
        w = np.array([1., 2.])
        utility = weighted_log(w)
        R = np.array([[1., 1.]])
        capacity = np.array([9.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(3. - res[0]) < DELTA)
        self.assertTrue(abs(6. - res[1]) < DELTA)

    def test_unshared_link(self):
        w = np.array([1., 2.])
        utility = weighted_log(w)
        R = np.array([[1., 0.], [0., 1.]])
        capacity = np.array([10., 10.])

        res = solve_num_problem(utility, R, capacity)
        self.assertTrue(abs(10. - res[0]) < DELTA)
        self.assertTrue(abs(10. - res[1]) < DELTA)

    def test_zero_capacity(self):
        w = np.array([1., 2.])
        utility = weighted_log(w)
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
        utility = proportionally_fair()

        solve_num_problem(utility, R, capacity)

    def test_large_weights(self):
        w = [1.,20.]
        R = [[1,1]]
        c = [10]
        solve_num_problem(weighted_log(w), R, c)

    def test_x0(self):
        R = [[1,1]]
        c = [10]
        solve_num_problem(proportionally_fair(), R, c, x0=[1,2])

if __name__ == '__main__':
    unittest.main()
