import pickle
import time
import winsound
import numpy as np
from scipy import optimize


def f_max1(func, x0, bounds=None):
    return -optimize.fmin_l_bfgs_b(func=lambda *t: -func(*t), x0=x0, approx_grad=True, bounds=bounds, maxfun=np.inf, maxiter=np.inf, epsilon=np.finfo(float).eps)[1]


def closed_ball(x, r):
    res = []
    for x_i in x:
        res.append((x_i - r, x_i + r))
    return res


def star_wars():
    with open("star_wars", "rb") as f:
        x = pickle.load(f)
        for fq, lt, dr in x:
            winsound.Beep(fq, lt)
            time.sleep(dr)
