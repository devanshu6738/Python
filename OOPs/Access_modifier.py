class Parent:
    def __init__(self,public,private,protected):
        self.public=public
        self._protected=protected
        self.__private=private

    def public(self):
        return "Hii from public method"
    
    def _protected(self):
        return "Hii from Protected method"
    
    def __private(self):
        return "Hii from Private method"
    

class Child(Parent):
    def AccessModifier(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

c1=Child()
c1.AccessModifier()
        