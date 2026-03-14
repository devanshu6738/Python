class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_detail(self):
        return f"{self.name}:{self.price}"

class Electronic(Product):
        def __init__(self,name,price,warranty):
            super().__init__(name,price)
            self.warranty=warranty

        def get_detail(self):
            return super().get_detail() + f" Warranty:{self.warranty}"   
        
class Clothing(Product):
     def __init__(self, name,price,size):
          super().__init__(name, price)
          self.size=size

     def getDetail(self):
          return super().get_detail() + f" size:{self.size}"     

phone=Electronic("Samsung",80000,1)
print(phone.get_detail())
cloth=Clothing("tshirt",1000,'M')
print(cloth.get_detail())