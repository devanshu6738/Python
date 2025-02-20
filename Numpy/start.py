import numpy as np
# List Vs Array
a=np.array([1,2,3,4,5],dtype='int32')
print(a)
print(a[0])
b=[2,"Devanshu","9june"]
print(b)
print(type(b))
print(type(a))
print(a[0]+a[1])
# 2d array
c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c)
print(c[1][1])
print(a.ndim)
print(c.ndim)    #check the dimension of the array
print(c.shape)   #check the number of the row and col
print(a.shape)
print(type(a))   #type of the datatype 
print(type(c))
print(a.itemsize)
print(c.itemsize)
print(c.size)
print(a.size)
print(a.dtype)
print(c.dtype)