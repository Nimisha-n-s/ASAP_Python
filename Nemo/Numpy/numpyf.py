#import numpy
#arr = numpy.array([1, 2, 3, 4, 5])
#print(arr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
#print(arr)
print(arr[1]) #array indexing
print(arr[0:5])
print(arr[5:10])
#print(arr[1:4])
arr1= np.array(42)  #zero dimensional array
arr2 = np.array([1, 2, 3, 4, 5]) #one dimensional array
arr3 = np.array([[1, 2, 3], [4, 5, 6]]) #two dimensional arry
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #three dimensional array

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)