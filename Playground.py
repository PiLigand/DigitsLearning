import random
import numpy


sizes = [6,4,4,2]
alph = [1,2,3,4]
bet = [9,8,7]
chrl = ['a','b','c','d']
metar = [alph,sizes,chrl]

#bias = [numpy.random.randn(y,1) for y in sizes[1:]]

#print (sizes[:-1])
#print (sizes[1:])

"""newat =zip(sizes, chrl)

for a, b in zip(sizes, bet):
    print (a*b) """

rands = numpy.random.randn(3,4)

print (rands.shape)
print (rands[2,2])
