class Camera:
    def take_photo(self):
        return "Taking a Photo"
    
class Phone:
    def Making_Call(self):
        return "Making a Phone Call"
    

class Smartphone(Camera,Phone):
    def browser(self):
        return "Browsering a Internet"
    

s1=Smartphone()
print(s1.Making_Call())