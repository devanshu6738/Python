import numpy as np
from numpy.random import randint as ri

arr=ri(1,10,20).reshape(4,5)
print(arr)
print(np.sum(arr))
print(np.prod(arr))
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print(np.prod(arr,axis=0))
print(np.prod(arr,axis=1))
print(np.mean(arr))

# variance and standard deviation
print(np.var(arr))
print(np.std(arr))
print(np.std(arr,axis=1))

# Median
print(np.median(arr))

# Percentile and quantiles

arr2=ri(1,10,20)
print(arr2)
print(np.percentile(arr2,50))
print(np.percentile(arr2,90))

# dot product
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(1,10).reshape(3,3)
print(np.dot(arr1,arr2))

# inner product and outer product

A=np.arange(1,6)  #sum of element wise product
B=ri(1,10,5)
print(np.inner(A,B))
if np.inner(A,B)==np.dot(A,B):
    print("Equal")

print(np.outer(A,B))

# Matrix Tranpose and Matrix Trace

arr=ri(1,10,20).reshape(5,4)
print(np.transpose(arr))
print(np.trace(arr))
print(np.trace(arr,offset=-1))
print(np.trace(arr,offset=1))
