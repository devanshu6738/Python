# without generic programming

def add (a:int,b:int)->int:
    return a+b

print(add(20,10))

# with generic programming

from typing import TypeVar

T=TypeVar('T')

def mul (a:'T',b:'T')->'T':
    return a*b

print(mul(10,29))