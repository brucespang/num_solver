import scipy.optimize
import numpy as np

def solve_num_problem(utility, R, capacity):
    num_resources,num_flows = R.shape

    # the scipy solver has problems if the capacity of any link is zero
    capacity = capacity.clip(min=0.00001)

    f = lambda x: -1*utility(x)
    x0 = np.array([1. for _ in range(num_flows)])

    res = scipy.optimize.minimize(f, x0,
                                  bounds=[(0., None) for _ in x0],
                                  constraints=[{'type': 'ineq',
                                                'fun': lambda x: np.asarray(capacity - np.dot(R, x)).flatten()}])

    if not res.success:
        print res
        raise Exception("Couldn't solve NUM problem")

    return res.x
