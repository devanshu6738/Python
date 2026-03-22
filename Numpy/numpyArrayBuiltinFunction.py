import numpy as np

print(list(range(1,50,2)))
arr=np.arange(10,20,dtype=np.float32)
print(arr)

# np.linspace
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

print(np.linspace(1,2,20))

# np.logspace()
# np.logspace (start, stop, num=50, endpoint=True, base 10.0, dtype=None)
# np.linspace(start, stop) gives values evenly spaced in linear space.
# np.logspace(start, stop) gives values evenly spaced in logarithmic space.

print(np.logspace(1,4,10))

print(np.logspace(0,10,5,base=2,dtype=np.int32))