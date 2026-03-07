# Student Management System

# Procedural Programming
student=[]
def AddStudent(name,standard,rollno):
    student.append({"name":name,"class":standard,"rollno":rollno})

def ShowDetail():
    for i in student:
        print(i)

AddStudent("Devanshu",10,2)
ShowDetail()