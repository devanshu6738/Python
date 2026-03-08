# custom decorator

def custom_decorator(func):
    def wrapper():
        print("something is happening before the func")
        func()
        print("something is happening after the func")
    return wrapper

# def hello_print():
#     print("Hello world")

# hello_prt=custom_decorator(hello_print)   #this is simple way
# hello_prt()


# now with custom decorator

@custom_decorator
def hello_print():
    print("Hello world")

hello_print()