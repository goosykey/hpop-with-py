import numpy as np


def funky_fun(t, y):
    dy = np.zeros_like(y)
    dy[0] = y[1]
    dy[1] = -9.81
    return dy
