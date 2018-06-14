import random
import numpy

sizes = [6,4,4,2]

#bias = [numpy.random.randn(y,1) for y in sizes[1:]]

#print (sizes[:-1])
#print (sizes[1:])

def sigmoid(x):
    return (1/(1+numpy.exp(-x)))

print (sigmoid(1))
