import struct

imagesPath = "train-images-idx3-ubyte"
imagesFile = open(imagesPath, "rb")

print("Magic Number: %i" % struct.unpack(">i", imagesFile.read(4))[0])

print("Number Entries: %i" % struct.unpack(">i", imagesFile.read(4))[0])

print("Images Rows: %i" % struct.unpack(">I", imagesFile.read(1))[0])

print("Images Cols: %i" % struct.unpack(">I", imagesFile.read(1))[0])
