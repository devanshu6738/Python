def Linear_Search(lst,x):
    for i in lst:
        if i==x:
            return True
    return False
        
lst=[20,67,45,43,78,90]

print(Linear_Search(lst,90))