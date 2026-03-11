# copy constructor 
# 1. shallow copy
# 2. deep copy

# 1. shallow copy

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def __copy__(self):
#         new_object=type(self)(self.name,self.age,self.marks)
#         return new_object
    
# s1=Student("Devanshu",21,[21,23,34])
# print(s1.marks)

# s2=s1.__copy__()
# print(s2.marks)

# print(id(s1.marks))
# print(id(s2.marks))
import copy

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

s1=Student("Devanshu",21,[92,87,67])
s2=copy.copy(s1)
s3=copy.deepcopy(s1)

print(id(s1.name),id(s2.name),id(s3.name))
