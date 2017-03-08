import unittest
import numpy as np
import num_solver

class TestNetworks(unittest.TestCase):
    def test_full_rank(self):
        rank = 8
        R,c = num_solver.generate_full_rank_topology(rank)
        self.assertEqual(np.linalg.matrix_rank(R), rank)

    def test_can_solve_generated_network(self):
        rank = 8
        R,c = num_solver.generate_topology(rank)
        num_solver.solve(num_solver.proportionally_fair(), R, c)


if __name__ == '__main__':
    unittest.main()
