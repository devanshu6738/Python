class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_Detail(self):
        return f"{self.name}:{self.price}"

class Electronic(Product):
        def __init__(self,name,price,warranty):
            super().__init__(name,price)
            self.warranty=warranty

        def getDetail(self):
            return super().get_Detail() + f" Warranty:{self.warranty}"   
        
class Clothing(Product):
     def __init__(self, name, price,size):
          super().__init__(name, price)
          self.size=size

     def getDetail(self):
          return super().get_Detail() + f" size:{self.size}"   

phone=Electronic("Samsung",80000,1)
print(phone.getDetail())
cloth=Clothing("tshirt",1000,'M')
print(cloth.getDetail())


class Animal:
     def __init__(self,name):
          self.name=name

     def speak(self):
          print(f"the animal speak {self.name}")

class Dog(Animal):
     def speak(self):          #Method Overriding
          print(f"the {self.name} brakes")


d1=Dog("Bruno")

d1.speak()
print(isinstance(d1,Dog))
print(isinstance(d1,Animal))

# Using super() 

class Vehicle:
     def __init__(self):
          print("constructor initialize")

     def start(self):
       print("vehicle started")

class Car(Vehicle):
     def __init__(self):
          super().__init__()
          print("Car constructor initialize")

     def start(self):
      print("Car started")
          

v1=Vehicle()
v1.start()
c1=Car()