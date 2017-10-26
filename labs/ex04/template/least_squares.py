# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    w_star = np.dot(np.dot(np.linalg.inv(np.dot(tx.T,tx)),tx.T),y)
    mse = np.sqrt(2*sum((y - np.dot(tx, w_star))**2)/(2*len(y)))
    return mse, w_star
    raise NotImplementedError
