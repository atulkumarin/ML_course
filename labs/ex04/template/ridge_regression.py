# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    w_star = np.dot(np.dot(np.linalg.inv(np.dot(tx.T,tx) + lambda_*2*tx.shape[0]*np.eye(tx.shape[1])),tx.T),y)
    mse = np.sqrt(2*sum((y - np.dot(tx, w_star))**2)/(2*len(y)))
    
    return mse, w_star
    raise NotImplementedError
