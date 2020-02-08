import numpy as np


def shear(y, x, coord):
    A = np.array([
        [1, x],
        [y, 1]
    ])
    return np.dot(A, coord)
