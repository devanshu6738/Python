from numpy.random import randint as ri
import numpy as np

arr=ri(1,100,10)
print(arr)
print(np.sort(arr))

arr2=ri(1,100,25).reshape(5,5)
print(arr2)
print(np.sort(arr2))

# axis 0: row changes, column will be constant
# axis 1: column changes, row will be constant

print(np.sort(arr2,axis=0))
print(np.max(arr2))

arr3=ri(1,31,10)
print(arr3)
print(arr3[1:11:2])
print(arr3[1:6])
print(arr3[::2])
print(arr3[::-1])
print(arr3[[1,3,8]])

arr4=np.array(ri(1,100,30)).reshape(5,6)
print(arr4)
# Entire column at index 3
print(arr4[:,3])

# Matrix with row indices 1 and 2 and column indices 3 and 4
print(arr4[1:3,3:5])
# subsetting
print(arr4[arr4>50])

mat= np.array([[11,12,13], [21,22,23], [31,32,33]])
mat_sliced=mat[:2,:2]
print(mat_sliced)