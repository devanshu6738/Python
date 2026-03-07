class Student:
    School_name="Carmel School"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def Display(self):
        print(f"Name:{self.name},Age:{self.age},Grade:{self.grade}")

def Print_Student_Detail(Student_Obj):
    Student_Obj.Display()

    
    


s1=Student("Devanshu",21,92)
Print_Student_Detail(s1)
