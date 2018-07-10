import struct

class DataSet(object):

    def __init__(self,  imagesPath = "train-images-idx3-ubyte", labelsPath = "train-labels-idx1-ubyte"):
        self.imagesFile = open(imagesPath, "rb")
        self.labelsFile = open(labelsPath, "rb")

        _magicNumbers()

        if (_checkEntries()):
            _pickImages()
            _pickLabels()
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
        self.ImagesList = []

        #For loop to cycle through each item / each image
        for i in range(0, self.imgCt):
            self.ImagesList.append([])
            #For loop for first dimmensions (to 28)
                Append
                #For loop for second dimmensions (to 28)
