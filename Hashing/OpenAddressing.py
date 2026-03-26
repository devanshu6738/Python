# openAddressing -> Dynamic Hashing Function
"""
1. Linear Probing
2. Quadratic Probing
3. Double Hashing
"""
# Linear Probing
Lst=[11,32,53,74,85,46,17,99,38,100]
def hashFind(HashTable,key):
    if(HashTable[key%10]==key):
        return key%10
    else:
        return None

HashTable=[None]*10

 
for i in range(0,len(Lst)):
    pass 

print(HashTable)

print(hashFind(HashTable,99))
print(hashFind(HashTable,59))