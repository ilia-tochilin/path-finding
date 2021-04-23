import numpy as np

class myArr:
    def __init__(self, array, rowLen):
        self.array = array
        self.counter = 0
        self.rowLen = rowLen
    
    ''' @var[dist] is 2 by def. because supr{all_dist} = 2 '''
    def push (self, value, exp = False, dist = 2):
        if (self.array.size <= self.counter):
            print ("Index Error")
            print ("{}  {}".format(self.counter, self.array.size))
            exit (1)
        self.array[self.counter]["val"] = value
        self.array[self.counter]["expanded"] = exp
        self.array[self.counter]["dist"] = dist
        self.counter += 1
    
    def __oneDout (self):
        for index, char in enumerate(self.array):
            if index % self.rowLen == 0:
                print ()
            print (char["val"], end="")
        print ()

    def __twoDout (self):
        for line in self.array:
            for char in line:
                print (char["val"], end="")
            print()

    def out (self):
        if self.array.ndim == 1:
            self.__oneDout()
        else:
            self.__twoDout()
    
    def getArray (self):
        return self.array