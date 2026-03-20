import numpy as np
print(np.__version__)

# 1d array

a1=np.array([1,2,3,4,5])
print(a1)
print(type(a1))
# print(help(np.array))

print(a1.shape)
print(a1.size)
print(len(a1))

# 2d array

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(arr2.shape)

# 3d array
arr3=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3)
print(arr3.shape)
print(arr3.size)

