def fun1():
    print("Hey")

fun1()

# a simple greeting function

def fun2(name):
    print(f'Hey {name}')

fun2("Devanshu")

# Using return in Function

def sum(num1,num2):
    return num1+num2

print(sum(3,4))

# Lambda function
greet=lambda name: f"Hello {name}" 

print(greet("Devanshu"))


#  Recursive function
# Factorial of a number

def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)

print(fact(5))

#  Map Function
data=[1,2,3,4,5]

def square(n):
    return n*n

print(list(map(square,data)))


#  reduce function
from functools import reduce

print(reduce(sum,data))

#  filter function

data=[1,2,3,4,5,6,7,8,9,10,11,12]

def check_even(num):
    if num%2==0:
        return True
    
print(list(filter(check_even,data)))

