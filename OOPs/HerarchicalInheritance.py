class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks !!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meow !!")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} sings Beautiful")


b1=Bird("chuchu")
b1.speak()

