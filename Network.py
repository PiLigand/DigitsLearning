# Basically cloning Micahel Nielsen's network code for MNIST digits for
#learning purposes only. Some differences may occur

# Standard Library
import random

#Third-Party Library.
import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.radn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
