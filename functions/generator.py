#  Generator function for the cube of the numbers

# Normal Implementation

for i in range(10):
    print(i*i*i)

# Generator Implementation

def gencubes(n):
    for val in range(n):
        yield val**3

for i in gencubes(10):
    print(i)

# practice question - fibonacci series through generator
