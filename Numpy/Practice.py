import numpy as np
from numpy import random as rnd
arr=np.array(rnd.randint(1,10,10)).reshape(2,5)
print(arr)

arr2=np.asarray(arr)
print(arr2)
print(arr2 is arr)

arr3=np.copy(arr)
print(arr3 is arr)

