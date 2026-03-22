# uniform distribution
# normal distribution
import numpy as np
# uniform distribution
print(np.random.rand(2,3))   #[0,1]
print(np.random.rand(2))
# normal distribution
print(np.random.randn(2,3))  #bell curve

#print random integer matrix

print(np.random.randint(1,100,20))
print(np.random.randint(1,100,(4,4)))