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

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b) # a (the neuron activations) is recursively cycled through each generation here
            # a is overwiritten each pass since we don't need to see the activations of hidden layers. The final layer is returned
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None): # eta is learning rate
        # training_data is a list of tuples (input image, label)
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs): # ranges here because xrange no longer exists
            random.shuffle(training_data)
            # mini_batches contains all training data, just blocked up into sections
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]

            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta) # Call to update_mini_batch function (defined below)

            if test_data: # Done to report progress on testing data set if present
                print ("Epoch {0}: {1}/{2}".format(j, self.evaluate(test_data), n_test)) # Call to evaluate function (defined below)
            else
                print ("Epoch {0} complete!".format(j))

    def update_mini_batch(self, mini_batch, eta):
        # this syntax wouldn't work with most lists, but these were defined as numpy arrays when they were first made
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch: # x is the input image and y is the label?
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights

    def backprop(self, x, y):




# Supporting functions
# When Numpy recieves a vector or a matrix, it will automatically apply this function element-wise:
    #(To each individual element)
def sigmoid(x): #The sigmoid function
    return (1/(1+np.exp(-x)))

def sigmoidPrime(x): #Derivative of the sigmoid function
    return sigmoid(x)*(1-sigmoid(x))
