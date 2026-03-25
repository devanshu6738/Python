import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=0))

print(arr.shape)

# Broadcasting

arr1=np.array([[1,2,3],[4,5,6]])  #(2,3)
arr2=np.array([1,2,3])       #(1,3)

print(arr1+arr2)

print(arr1+5)

# Vectorization

print(arr+arr1)
print(arr*arr1)
print(arr-arr1)

# Vectorization vs Loops
# Squaring 10 millions numbers
import time
N=10000000
arr=np.arange(N)
print(arr.shape)
current_time=time.time()
res_loop=[x**2 for x in arr]
print(time.time()-current_time)
arr=np.arange(N)
current_time=time.time()
arr=arr**2
print(time.time()-current_time)






