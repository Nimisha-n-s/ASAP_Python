#you are given a numpy array that represents a grid of numbers.write a funstion that perform the following operations:
#1)Replace all even numbers in the array with the square
#2)Replace all odd numbers in the array with their cubes
#3) find the sum of the modified array
#reshape the array into a new shape provided by the user if possible.if reshaping is not possible,print a message 

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Original array:\n", arr)
print("shape=",arr.shape)


#replacing
def new():
    for i in range(len(arr)):
        for j in range(len(arr[i])): 
            if arr[i, j] % 2 == 0:
                arr[i, j] = arr[i, j] ** 2
            else:
                arr[i, j] = arr[i, j] ** 3

new()
print("Modified array:\n", arr)

#reshaping
def reshape():
    newarr= arr.reshape(5,2)
    print("reshaped=",newarr)
reshape()

