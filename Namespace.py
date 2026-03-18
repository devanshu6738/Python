# amespace in Python is a container that acts as a mapping from names (identifiers like variable, function, and class names) to their corresponding objects in memory. It is implemented as a dictionary and ensures that each name is unique within its context, preventing naming conflicts in a program

def greeting():
    print("Hello this is my vscode")

print(globals())

def name():
    my_name="Devanshu Gupta"
    print(locals())

name()

print(dir(__builtins__))

# The dir() function in Python is a built-in introspection tool used to list the attributes and methods of an object or the names in the current local scope

# print(dir())

