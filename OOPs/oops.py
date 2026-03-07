# class define
class Student:
    School_name="Carmel School"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    # pass

s1=Student("Devanshu",21,92)
print(s1.name)
# print(type(Student))

s1.name="Dev"
print(s1.name)
print(s1.School_name)