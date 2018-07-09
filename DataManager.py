import struct

class DataSet(object):

    def __init__(self, imagesPath = "train-images-idx3-ubyte", labelsPath = "train-labels-idx1-ubyte"):
        self.imagesFile = open(imagesPath, "rb")
        self.labelsFile = open(labelsPath, "rb")
        self._pickLabels()


    def _pickLabels(self):
        print(struct.unpack(">i", self.labelsFile.read(4))[0])
