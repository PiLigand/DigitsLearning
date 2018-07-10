import struct
import numpy

class DataSet(object):

    def __init__(self,  imagesPath = "train-images-idx3-ubyte", labelsPath = "train-labels-idx1-ubyte"):
        self.imagesFile = open(imagesPath, "rb")
        self.labelsFile = open(labelsPath, "rb")

        _magicNumbers()

        if (_checkEntries()): # Should form list of images and corresponding list of labels
            _pickImages()
            _pickLabels()
            _wrapLabels()
        else:
            print("Image/label count mismatch.")

            # Close opened files after collecting important data
            self.imagesFile.close()
            self.labelsFile.close()

    def _magicNumbers(self): # ust prints magic numbers for each data file opened. Could very well be ignored.
        #Files should be read here to maintain correct reading sequence of bytes, but printing could be omitted to save output
        self.imgMN = struct.unpack(">i", self.imagesFile.read(4))[0]
        self.lblMN = struct.unpack(">i", self.labelsFile.read(4))[0]
        #Comment these lines to neglect output
        print ("Images Magic Number: " + self.imgMN)
        print ("Labels Magic Number: " + self.lblMN)

    def _checkEntries(self): # Returns a quick boolean check to make sure there are the correct number of entries for each list.
        self.imgCt = struct.unpack(">i", self.imagesFile.read(4))[0]
        self.lblCt = struct.unpack(">i", self.labelsFile.read(4))[0]
        #Can comment these to neglect the output.
        print ("Images Count: " + self.imgCt)
        print ("Labels Count: " + self.lblCt)

        return (imgCt == lblCt)

    def _pickImages(self):
        # For MNIST files as of 07/09/18, these values should each be 28 (integer)
        self.imgRows = struct.unpack(">i", self.imagesFile.read(4))[0]
        self.imgCols = struct.unpack(">i", self.imagesFile.read(4))[0]

        #Initialize empty list. Each item will have a two dimmensional list within
        self.imagesList = []

        #For loop to cycle through each item / each image
        for i in range(0, self.imgCt):
            self.imagesList.append([])
            #For loop for first dimmensions (Rows to 28)
            for j in range(0, self.imgRows):
                self.imagesList[i].append([])
                #For loop for second dimmensions (Columns to 28)
                for k in range(0, self.imgCols):
                    point = struct.unpack(">f", self.imagesFile.read(1))[0]
                    self.imagesList[i][j].append(point)

    def _pickLabels(self): #Makes a list of all labels in order
        self.labelsList = numpy.zeros(self.lblCt, numpy.int8) #Initializes a numpy array of correct size
        self.labelsList = [struct.unpack(">i", self.labelsFile.read(1))[0] for i in self.labelsList] #Sets all values of labels from file

    def _wrapLabels(self): # Creates a new list - one for each label - of ten-item lists
    # Each label returns a list of zeros except for the position i which will hold 1.0
        self.wrapLabels = []
        for i in range(0, self.lblCt):
                                    #0    1    2    3    4    5    6    7    8    9
            self.wrapLabels.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
            self.wrapLabels[i][self.labelsList[i]] = 1.0

    def images(self):
        return self.imagesList

    def labels(self):
        return self.labelsList

    def wrappedLabels(self):
        return self.wrapLabels

    def NielsenTuple(self): # Included specifically to return data in the format Nielsen uses
