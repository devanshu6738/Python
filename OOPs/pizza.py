class Pizza:
    def __init__(self,size,toppings):
        self.size=size
        self.toppings=toppings

    def bake(self):
        print(f"Baking a pizza of size- {self.size} and toppings - {','.join(self.toppings)}")

    def serve(self):
        print("your pizza is now ready to serve")

    def __str__(self):
        return f"hey !! my order is {self.size} pizza toppings with {','.join(self.toppings)}"

    

p1=Pizza("medium",["paneer","mushroom"])
print(p1)
p1.bake()
p1.serve()


requestPizza_by_Devanshu= [
[4, "Large", ["cheese", "panner", "capsicum"]],
[1, "Medium", ["mushroom", "olives"]],
[2, "Small", ["cheese", "panner", "capsicum"]],
[3, "Small", ["mushroom", "olives"]]
]

request_for_Devanshu=[]

for req in requestPizza_by_Devanshu:
    for idx in range(req[0]):
        pizza_obj=Pizza(req[1],req[2])
        pizza_obj.bake()
        pizza_obj.serve()

        request_for_Devanshu.append(pizza_obj)
        


