# Self-built modules
import Network
import DataManager

# Third-party modules
import numpy

# Built-in modules
import struct

MNIST = DataManager.DataSet()

training_data, validation_data, test_data = MNIST.NielsenTuple(50000, 10000, 10000)
