# this is a simple example for hashing
Lst=[11,32,53,74,85,46,17,99,38,100]
def hashFind(HashTable,key):
    if(HashTable[key%10]==key):
        return key%10
    else:
        return None

HashTable=[None]*10
 
for i in range(0,len(Lst)):
    HashTable[Lst[i]%10]=Lst[i]

print(HashTable)

print(hashFind(HashTable,99))
print(hashFind(HashTable,59))

# Implementation through Dictionary

HashTable={}
Lst=[11,32,53,74,85,46,17,99,38,100]
for i in range(0,len(Lst)):
    HashTable[Lst[i]%10]=Lst[i]

print(HashTable)

print(hashFind(HashTable,32))
