class EmptyClass:
    pass

class ChildEmptyClass(EmptyClass):
    pass
c=EmptyClass()
print(dir(c))

d=object()
print(dir(d))

print(type(EmptyClass))
print(isinstance(EmptyClass,object))
print(isinstance(super,object))
print(isinstance(ChildEmptyClass,EmptyClass))