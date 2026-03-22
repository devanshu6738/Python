import numpy as np

# numpy array and matrix creation

# vector and matrix of zero

print(np.zeros(5))
print(np.zeros((3,3)))

# vector and matrix of ones

print(np.ones(5))
print(np.ones((5,5)))

# vector and matrix of any number

print(np.ones(5)*4)
print(np.ones((5,5))*4)

# np.empty- it just create a matrix and initialize the value with garbage value

print(np.empty((4,3)))


# np.reshape()
# Diagonal, Triangular, Lower Triangular and Upper Triangular Matrix

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.diag(arr))

print(np.triu(arr))
print(np.tril(arr))

print(np.diag(np.diag(arr)))  #diagonal matrix


# np.eye()
# np.eye (N, M=None, k=0, dtype=float, order='C')

print(np.eye(3))



# The numpy.reshape() function (often used as np.reshape()) is used to change the shape (dimensions) of a NumPy array without changing the data it contains. It returns a new array with the specified configuration
x=np.arange(9).reshape((3,3))
print(x)
print(np.diag(x))
print(np.diag(x,k=-2))
print(np.diag(x,k=-1))
print(np.diag(x,k=0))
print(np.diag(x,k=1))
print(np.diag(x,k=2))

# NumPy allows triangular functions like np.tril() and np.triu() to operate on rectangular matrices for flexibility and general-purpose use -even though the strict mathematical definition of triangular matrices only applies to square matrices.

print(np.tri(3,5,0))

arr2 = np.array([[1,2,3], [4,5,6],[7,8,9], [10,11,12]])
print(arr2)

print(np.tril(arr2,-1))