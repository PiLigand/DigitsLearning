# Self-built modules
import Network
import DataManager

# Third-party modules
import numpy

# Built-in modules
import struct

arr1 = numpy.array([[1,2,3], [4,5,6]])
print(" ==================== arr1 ======================")
print(arr1)
print(arr1.shape)

arr2 = numpy.array([7,8,9])
print(" ==================== arr2 ======================")
print(arr2)
print(arr2.shape)

arr3 = numpy.dot(arr1, arr2)
print(" ==================== arr3 ======================")
print(arr3)
print(arr3.shape)

arr4 = numpy.array([11,22])
print(" ==================== arr4 ======================")
print(arr4)
print(arr4.shape)

arr5 = arr3 + arr4
print(" ==================== arr5 ======================")
print(arr5)
print(arr5.shape)
