import struct

def dataSet(imagesPath = "train-images-idx3-ubyte", labelsPath = "train-labels-idx1-ubyte"):
    imagesFile = open(imagesPath, "rb")
    labelsFile = open(labelsPath, "rb")

    imagesList = []
    labelsList = []

    _magicNumbers(imagesFile, labelsFile)

    if (_checkEntries(imagesFile, labelsFile)):
        imagesList = _pickImages(imagesFile)
        labelsList = _pickLabels(labelsFile)
    else:
        print("Image/label count mismatch.")

    # Close opened files just before returning important data
    imagesFile.close()
    labelsFile.close()

    return imagesList, labelsList

def _magicNumbers(images, labels): # ust prints magic numbers for each data file opened. Could very well be ignored.
    #Files should be read here to maintain correct reading sequence of bytes, but printing could be omitted to save output
    print ("Images Magic Number: " + struct.unpack(">i", images.read(4))[0])
    print ("Labels Magic Number: " + struct.unpack(">i", labels.read(4))[0])

def _checkEntries(images, labels): # Returns a quick boolean check to make sure there are the correct number of entries for each list.
    imgCt = struct.unpack(">i", images.read(4))[0]
    lblCt = struct.unpack(">i", labels.read(4))[0]
    print ("Images Count: " + imgCt)
    print ("Labels Count: " + lblCt)

    return (imgCt == lblCt)
