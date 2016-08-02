import numpy as np

def proportionally_fair():
    return lambda x: np.ma.sum(np.ma.log(x))

def weighted_log(w):
    return lambda x: np.dot(w, np.ma.log(x))

def stcp():
    return weighted_log(80)