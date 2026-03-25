import numpy as np
from numpy.random import randint as ri

mat1=np.array(ri(1,21,9).reshape(3,3))
mat2=np.array(ri(1,21,9).reshape(3,3))
print(mat1)
print(mat2)
print(mat1+mat2)
print(mat1*mat2)
print(mat1/mat2)
print(2*mat1-3*mat2)
print(mat1+100)
print(mat1**2)
print(pow(mat1,0.5))

mat3=np.array(ri(1,21,6).reshape(2,3))
print(mat3)
mat3=mat3.T  #Tranpose
print(mat3)
