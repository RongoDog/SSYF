#! python

import numpy as np

class Connection:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.weights = np.random.random((l1.size, l2.size)) - 1 
