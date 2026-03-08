# In Python, Dunder methods are special methods whose names start and end with double underscores.
# They are also called Magic Methods or Special Methods.    

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __str__(self):
    #     print(self.name)
    #     print(self.age)

s1=Student("Devanshu",21)
s1.__str__() 
print(s1)

# print([1,2,3].__len__())

