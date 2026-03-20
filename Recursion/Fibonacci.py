def Fibonnaci(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return Fibonnaci(n-1)+Fibonnaci(n-2)

print(Fibonnaci(10))