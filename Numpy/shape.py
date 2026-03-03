import numpy as np


# shape =(block,row,col)
arr2d=np.array([[1,2,3],[4,5,6]])
print(arr2d.shape)

arr3d=np.array([[[1,2,3],[1,2,3,]],[[4,5,6],[4,5,6]]])
print(arr3d.shape)


#Broadcasting in the numpy

print(arr2d+5)


A=np.array([[1,2,3],[4,5,6]])
B=np.array([11,12,13])
C=A+B
print(C)