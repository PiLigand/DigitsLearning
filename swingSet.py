import struct
import DataManager

imagesPath = "train-images-idx3-ubyte"
labelsPath = "train-labels-idx1-ubyte"
imagesFile = open(imagesPath, "rb")
labelsFile = open(labelsPath, "rb")

print("Magic Number: %i" % struct.unpack(">i", labelsFile.read(4))[0])

print("Number Entries: %i" % struct.unpack(">i", labelsFile.read(4))[0])


#print("Images Rows: %i" % struct.unpack(">i", imagesFile.read(4))[0])
#print("Images Cols: %i" % struct.unpack(">i", imagesFile.read(4))[0])

for i in range(0, 784): #Should be first image in set
    print("Label %i: %i" % (i, struct.unpack(">B", labelsFile.read(1))[0]))


imagesFile.close()
labelsFile.close()
