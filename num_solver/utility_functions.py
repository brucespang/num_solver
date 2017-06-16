from __future__ import division
import numpy as np

def proportionally_fair():
    return lambda x: (np.ma.sum(np.ma.log(x)), 1/x)

def weighted_log(w):
    w = np.divide(w, float(np.amax(w)))
    return lambda x: (np.dot(w, np.ma.log(x)), np.ma.divide(w, x))

def stcp():
    return weighted_log(80)

def multipath_proportionally_fair(H):
    return lambda x: (np.sum(np.log(np.dot(H,x))), np.dot(1/np.dot(H,x), H))

def vegas(RTT, alpha=None):
    if alpha is None:
        alpha = [4]*len(RTT)
    return weighted_log(np.multiply(alpha, RTT))

def reno(RTT):
    return lambda x: np.sqrt(2)/RTT*np.arctan2(RTT*x, np.sqrt(2))
