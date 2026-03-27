import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint as ri

A=np.array(ri(1,100,20))  #Assume number of Rooms
B=np.array(ri(1,1000,20)) #price of house
print(A,B)
print(np.corrcoef(A,B))
# plt.scatter(A,B)
# plt.show()

A=np.array(ri(50,100,20))
B=2*A+10*np.random.randn(20)
print(A,B)
plt.scatter(A,B)
plt.show()
print(np.corrcoef(A,B))