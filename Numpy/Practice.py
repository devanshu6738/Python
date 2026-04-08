import numpy as np
from numpy import random as rnd
arr=np.array(rnd.randint(1,10,10)).reshape(2,5)
print(arr)

arr2=np.asarray(arr)
print(arr2)
print(arr2 is arr)

arr3=np.copy(arr)
print(arr3 is arr)

print(arr.shape)

print(list(range(5)))

print(np.arange(1,50,2,dtype='int32'))

print(np.linspace(1,100,num=20,endpoint=False))
print(np.linspace(1,100,num=20,endpoint=True))


print(np.linspace(1,100,num=20,endpoint=True,retstep=True))

print(np.logspace(1,50,num=20,endpoint=True))

print(np.zeros((3,4)))

print(5*np.ones((3,4)))