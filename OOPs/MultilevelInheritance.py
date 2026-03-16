class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks !!")


class Labrador(Dog):
    def swin(self):
        print(f"{self.name} can swim")


l1=Labrador("Bruno")
l1.swin()

l1.speak()