#Little file to play with creating and structuring classes

class swing(object):
    def __init__(self, a=2, b=3):
        self.c=newFunction(a,b)

    def getC(self):
        return self.c

# Normally functions need to be above their uses, but sinc this is all imported,
# this is technically compiled prior to being run?
# Functions used by classes can be below thier class.
def newFunction(a, b):
    return ((a+b)*a)
