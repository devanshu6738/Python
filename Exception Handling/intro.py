# print(10/0)
print(int("1234"))
# print(int("abc"))

# exception is a runtime error that python can catch and handle using try-except

# there is my type of exception
# Value error
# divide by zero error
# type error
# and many more...

# type error
# print("5"+10)

# NameError
# print(y)

# Value Error
# print(int("abc"))

# Division by zero
# print(5/0)

# File Not Found Error
# with open("dev.txt","r") as f:
#     content=f.read

# indexError
# lst=[1,2,3]
# print(lst[4])

try:
    print("5"+10)
except Exception as e:
    print(f"Exception raised - {e}")


# Syntax error
# if True
#      print("hello")


# Indentation error
# if True:
# print("hello")

# Why Use Exception Handling?
# Prevent program crashes
# Handle unexpected user input or system errors
# Provide meaningful error messages
# Ensure resources are properly released (e.g., file handles, network connections)

try:
    result=10/0
except ZeroDivisionError:
    print("Error: divide zero is invalid and runtime error")


try:
    result=10/0
except ZeroDivisionError:
    print("Error: divide zero is invalid and runtime error")
except ArithmeticError:
    print("Error: It is a Arithmetic Error")

# Finally: The finally block contains code that will be executed regardless of whether an exception occurred or not. It is useful for cleanup operations.
# It ensures that important actions always happen, such as:
# Closing files
# Releasing resources
# Disconnecting from a database
# Releasing a lock
# Logging an operation

try:
   result = 10/0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block executed")


try:
    result=10/0
except ZeroDivisionError:
    print("Error: Divide by Zero")
else:
    print("No exception found")


# Raise: The raise statement is used to manually raise an exception. This can be useful when you want to indicate that a certain condition is an error.

age=-1
if age<0:
    raise ValueError("Age must be Non-Negative")