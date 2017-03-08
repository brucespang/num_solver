import fnss
import numpy as np

def generate_topology(num_nodes):
    topology = fnss.topologies.randmodels.barabasi_albert_topology(num_nodes, 2, 3).adjacency_list()

    R = np.array([[int(n in neighbors) for n in range(num_nodes)] for neighbors in topology])

    capacity = np.random.uniform(100, size=R.shape[0])+1

    min_R = []
    min_capacity = []

    return R,capacity

def generate_full_rank_topology(num_nodes):
    while True:
        R,c = generate_topology(num_nodes)
        if np.linalg.matrix_rank(R) == num_nodes:
            return R, c
