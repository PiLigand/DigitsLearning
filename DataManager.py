import struct

class DataSet(object):

    def __init__(self, imagesPath = "train-images-idx3-ubyte", labelsPath = "train-labels-idx1-ubyte"):
        self.imagesFile = open(imagesPath, "rb")
        self.labelsFile = open(labelsPath, "rb")

    def _pickLabels(self):
        
