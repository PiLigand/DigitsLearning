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
        self.imagesList = numpy.zeros((self.imgCt, self.imgRows, self.imgCols))

        #For loop to cycle through each item / each image
        for i in range(0, self.imgCt):
            #For loop for first dimmensions (Rows to 28)
            for j in range(0, self.imgRows):
                #For loop for second dimmensions (Columns to 28)
                for k in range(0, self.imgCols):
                    self.imagesList[i][j][k] = struct.unpack(">f", self.imagesFile.read(1))[0]

    def _pickLabels(self): #Makes a list of all labels in order
        self.labelsList = numpy.zeros(self.lblCt, numpy.int8) #Initializes a numpy array of correct size
        self.labelsList = [struct.unpack(">i", self.labelsFile.read(1))[0] for i in self.labelsList] #Sets all values of labels from file

    def _wrapLabels(self): # Creates a new list - one for each label - of ten-item lists
    # Each label returns a list of zeros except for the position i which will hold 1.0
        self.wrapLabels = numpy.zeros((self.lblCt, 10))
        #Changes appropriate number in each label to 1.0
        for i in range(0, self.lblCt):
            self.wrapLabels[i][self.labelsList[i]] = 1.0

    def images(self):
        return self.imagesList

    def labels(self):
        return self.labelsList

    def wrappedLabels(self):
        return self.wrapLabels

    def NielsenTuple(self, train, val, test): # train val and test are ints that count the entries for training_data, valiation_data, and test_data. Probs 50k, 10k, 10k
        # Included specifically to return data in the format Nielsen uses in his load_data_wrapper()
        linearImages = [numpy.reshape(ar, (self.imgRows*self.imgCols)) for ar in self.imagesList]

        training_data = [self.linearImages[x], self.wrapLabels[x] for x in range(0, train)] # Tuple of first [50k] linear image entries with their wrapped labels
        test_data = [self.linearImages[x], self.imageLabels[x] for x in range(train, train+test)] #Tuple of next [10k] linear image entries with int labels

        validation_data = [self.linearImages[x], self.imageLabels[x] for x in range(0, self.imgCt)] # Tuples all linear images with int labels
        numpy.random.shuffle(validation_data)   # Shuffels said entries. Still tuple'd, but now in a randowm order
        validation_data = validation_data[:val] # Trims to only first [10k or val] linear image entries requested for validation. With int labels

        return training_data, validation_data, test_data
