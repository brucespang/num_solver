# Network Utility Maximization Solver

A tool for solving [Network Utility Maximization](http://www.ifp.illinois.edu/~srikant/ECE567/Fall09/lecture2-num-primal.pdf) problems.

```
$ pip install num_solver
```

## Example

```
$ python
Python 2.7.11 (default, Jan 22 2016, 08:29:18)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import num_solver
>>> import numpy as np
>>> utility = lambda x: np.sum(np.ma.log(x))
>>> R = np.array([[1., 1.]])
>>> capacity = np.array([10.])
>>> num_solver.solve_num_problem(utility, R, capacity)
array([ 5.,  5.])
```
