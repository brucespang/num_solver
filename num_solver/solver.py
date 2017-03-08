import scipy.optimize
import numpy as np

def solve_num_problem(utility, R, c, maxiter=1000, tol=1e-10, x0=None):
    R = np.array(R)
    c = np.array(c)

    num_links,num_flows = R.shape[0],R.shape[1]
    if x0 is None:
        x0 = np.array([1.]*(num_flows+num_links))

    # the scipy solver has problems if the capacity of any link is zero
    c = c.clip(min=1e-5)

    def rates(variables):
        return variables[0:num_flows]

    def prices(variables):
        return variables[num_flows:]

    f = lambda v: -1*utility(rates(v))[0]

    res = scipy.optimize.minimize(f, x0,
                                  bounds=[(0., None) for _ in range(num_links+num_flows)],
                                  constraints=[{'type': 'eq','fun': lambda v: utility(rates(v))[1] - np.dot(R.T, prices(v))},
                                               {'type': 'eq','fun': lambda v: np.dot((c - np.dot(R,rates(v))), prices(v))},
                                               {'type': 'ineq','fun': lambda v: c - np.dot(R, rates(v))}
                                             ],
                                  options={
                                      'maxiter': maxiter
                                  },
                                  tol=tol)

    if not res.success:
        print res
        raise Exception("Couldn't solve NUM problem")

    rates = rates(res.x)
    return rates

def solve(*args):
    return solve_num_problem(*args)
