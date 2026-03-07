# In Python, Getter and Setter methods are used to access and modify private variables of a class in a controlled way.

#  using getter and setter in student management system

class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def getterStudent(self):
        print(self._name,self._age)

    def setterStudentAge(self,age):
        self._age=age
        print(self._age)

s1=Student("Devanshu",21)
s1.getterStudent()
s1.setterStudentAge(22)

