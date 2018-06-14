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
        #Goes from one dimmension to two. Holds biases, one for each neuron in a hidden layer and output layer
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        #Two dimmensions to three. Each hidden/output neuron gets weights from each prev generation neuron.
        #Cycles through sizes using sizes[R] for rows and sizes[R-1=C] for columns, thus the offset.
        self.weights = [np.random.radn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]



# Supporting functions
def sigmoid(x): #The sigmoid function
    return (1/(1+np.exp(-x)))

def sigmoidPrime(x): #Derivative of the sigmoid function
    return sigmoid(x)*(1-sigmoid(x))
