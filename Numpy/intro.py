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

arr4=np.array([1,2,3,4],ndmin=2)
print(arr4)

arr5=[1,2,3,4]
print(type(arr5))
a=np.asarray(arr5)
print(type(arr5))
print(type(a))

# If dtype is set, array is copied only if dtype does not match:

b=np.array([1,2,3,4,5],dtype=np.int32)
print(np.asarray(b) is b)

# copy

c=np.array(b,copy=False)
print(c)
print(c is b)

# Create an array x, with a reference y and a copy z
d=c
print(id(d))
print(id(c))
e=np.copy(c)
print(id(e))

# Read and write data from a file



# binary file
arr6=np.array([1,2,3,4,5])
np.save("array.npy",arr6)
arr7=np.load("array.npy")
print(arr7)


# save multiple array
np.savez("array1.npz",arr1=a,arr2=b)
data1=np.load("array1.npz")
print(data1["arr1"])
print(data1["arr2"])

# np.fromfunction()
