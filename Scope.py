y=7
def test():
    print(y)

test()

def test2():
    y=10
    print(y)

test2()
print(y)

def greet():
    msg="Hello How are you"  #Local Variable
    print(msg)


# print(msg)

# Enclosing Scope
def greet_outer():
    msg="Hello How are you guys ??"

    def greet_inner():
        print(msg)

    greet_inner();

greet_outer();

# Global Scope

msg1="Hello Myself Devanshu"
def greet1():
    print(msg1)

greet1()

def greet2():
    global msg1
    msg1="Hello this my ai ml journey"
    print(msg1)

greet2()

# LEGB Rule

ans="Devanshu"
def func1():
    ans="AI ML"
    print(ans)

func1()
