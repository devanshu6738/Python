class Myclass:
    def add(self,*args):
        return sum(args)
    
ad=Myclass()
result=ad.add(1,2,3,4,5)
print(result)