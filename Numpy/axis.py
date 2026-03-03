import numpy as np

#for 2d data axis=0 column wise
arr2d=np.array([[1,2,3],[4,5,6]])
print(np.sum(arr2d,axis=0))

#for 3d data axis=0 column wise

arr3d=np.array([[[1,2,3],[1,2,3,]],[[4,5,6],[4,5,6]]])
print(np.sum(arr3d,axis=0))

arr2d=np.array([[1,2,3],[4,5,6]])
print(np.sum(arr2d,axis=1))


