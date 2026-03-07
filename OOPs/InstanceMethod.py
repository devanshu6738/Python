class Student:
    School_name="Carmel School"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def Display(self):
        print(f"Name:{self.name},Age:{self.age},Grade:{self.grade}")

    def __str__(self):
        return f"Hello myself {self.name} age {self.age} grade {self.grade} School {self.School_name}"
    
    @classmethod
    def change_schoolName(cls,sc_name):
        cls.School_name=sc_name


s1=Student("Devanshu",21,92)
s1.Display()

print(s1.__str__())
s1.School_name="Carmel Convent School"

print(s1.__str__())

print(Student.School_name)