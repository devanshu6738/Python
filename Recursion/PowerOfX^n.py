def PowerofXn(x,n):
    if n==0:
        return 1
    return x*PowerofXn(x,n-1)

print(PowerofXn(9,2))