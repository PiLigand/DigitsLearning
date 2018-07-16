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
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

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
            else:
                print ("Epoch {0} complete!".format(j))

    def update_mini_batch(self, mini_batch, eta):
        # this syntax wouldn't work with most lists, but these were defined as numpy arrays when they were first made
        # Also, Cost is a function of weights and biases, but here they are simply separated into their own vectors
            # for ease of application. The spearation has no mathematical signifigance.
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch: # x is the input image and y is the label - the right answer.
            delta_nabla_b, delta_nabla_w = self.backprop(x, y) # Figures out how much to change each variable.
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)] # Is this where the averaging is done? We'll see

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # Feed Forward Section calculating z, then sigmoid to get each layer of activation
        activation = x # Activation of first layer
        activations = [x] # List to store layer of activations. Will add layers as we go.
        zs = [] # List to store z vectors (what will be sigmoided) Will add layers as we go
        for b, w in zip(self.biases, self.weights): # Goes through layer by layer, calculating activations of layers from previous layers
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        # Back Propogation section
        # activations[-1] is the output layer, y is a number label. array[-1] gives the last element in that array.
        delta = self.cost_derivative(activations[-1], y) * sigmoidPrime(zs[-1]) # A piece of an equation that we need twice. In d/dw, d/da and d/db
        nabla_b[-1] = delta # No further components
        nabla_w[-1] = np.dot(delta, activations[-2].transpose()) # nx1 nx1T ->  nx1 1xn = nxn matrix

        for l in range(-2, -self.num_layers, -1):
            z = zs[l]
            sp = sigmoidPrime(z)
            delta = np.dot(self.weights[l+1].transpose(), delta) * sp
            nabla_b[l] = delta
            nabla_w[l] = np.dot(delta, activations[l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x,y) in test_results)

    def cost_derivative(self, output_activations, y): # y is a number label
        # y is a list representing ideal network output, not an integer. Setup in the data mover/wrapper, not in MNIST
        return (output_activations - y) # d[(a-y)^2] proportional to. Can ignore the resulting 2 factor. ultimately eta controlled.



# Supporting functions
# When Numpy recieves a vector or a matrix, it will automatically apply this function element-wise:
    #(To each individual element)
def sigmoid(x): #The sigmoid function
    return (1/(1+np.exp(-x)))

def sigmoidPrime(x): #Derivative of the sigmoid function
    return sigmoid(x)*(1-sigmoid(x))

def relu(x): # The Rectified Linear Unit (ReLU) function. To replace sigmoid
    if (x <= 0):
        return 0
    else:
        return x

def reluPrime(x): #Derivative of the relu function
    if (x <= 0):
        return 0
    else:
        return 1
