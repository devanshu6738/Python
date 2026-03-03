# design a student management system using proceedural programming and OOPS

students=[]
 
def addStudent(name,age,grade):
    students.append({'name':name,'age':age,'grade':grade})

def displayStudent():
    for s in students:
        print({s['name'],s['age'],s['grade']})

addStudent("Devanshu",20,9)
addStudent("Ayush",20,10)
addStudent("Shubham",20,10)
displayStudent()

# Limitations in Procedural:
# Global variable students risky in large codebases
# Data (dict) and behavior (add, display) are separate
# any code can change student data incorrectly No protection
# Can't easily create multiple independent student groups

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

        def display(self):
            print("Name:{self.name},Age:{self.age},Grade:{self.garde}")


