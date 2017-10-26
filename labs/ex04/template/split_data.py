# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    data_size = len(y)
    train_size = int(np.floor(data_size*ratio))
    
    shuffled_ind = np.random.permutation(np.arange(data_size))
    
    train_x = x[shuffled_ind][0:train_size]
    train_y = y[shuffled_ind][0:train_size]
    test_x = x[shuffled_ind][train_size:]
    test_y = y[shuffled_ind][train_size:]
    return train_x, train_y, test_x, test_y
    raise NotImplementedError
