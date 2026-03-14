class User:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password

    def login(self,enterPassword):
        if self.__password==enterPassword:
            return f"username:{self.__username} password:{self.__password}"
        else:
            return f"Incorrect Password"
        
u1=User("Devanshu","devanshu")
print(u1.login("Devanshu"))
print(u1.login("devanshu"))
    