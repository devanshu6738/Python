class Car:
    wheels=4
    def __init__(self,brand):
        self.brand=brand

car1=Car("toyota")
car2=Car("Mahindra")

print(car1.wheels)
print(Car.wheels)
print(car2.wheels)

Car.wheels=6
print(car1.wheels)
print(Car.wheels)
print(car2.wheels)


# utility method
class my_utilityMethod:
    @staticmethod
    def square(num):
        return num*num
    
print(my_utilityMethod.square(10))

# factory method

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def create(name,age):
        if age<18:
            raise ValueError("You are not eligible")
        return User(name,age)
    
user1=User("Devanshu",21)
user2=User("Devanshu",14)
print(user1.name)
print(user2.name)

