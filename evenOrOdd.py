# simple list filter 
# firstly, multiply all number inside in array
# if total = even, it return total sum of array
# if total = odd, it return 0

import numpy

class numFilter:
    def __init__(self, inputAry):
        self.inputAry = inputAry

    def procOp(self):
        total = numpy.prod(self.inputAry)
        print("Multiply of List = ", total)
        if (total % 2 == 0):
            print("The List is Even")
            sum1 = sum(self.inputAry)
            print("The Sum of list = ",sum1,"\n")
        else:
            print("The List is Odd\n")

# For Odd sample list
input1 = [1,3,1,3]
print("\nList of Input Array = ", input1)
test1 = numFilter(input1)
test1.procOp()

# For Even sample list
input2 = [1,2,4,3]
print("\nList of Input Array = ", input2)
test2 = numFilter(input2)
test2.procOp()
