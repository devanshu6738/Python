# Implementation of hashing through chaining in Hashing

class HashTableChaining:
    def __init__(self,size=10):
        self.size=size
        self.table=[[] for i in range(size)]

    def InsertValue(self,value):
        self.table[value%10].append(value)
        print(self.table)
        print(self.table[0])

    def HashSearch(self,value):
        for i in self.table[value%10]:
            if i==value:
                return True
            else:
                return False
    def HashDelete(self,value):
        for i in self.table[value%10]:
            if i==value:
                return self.table[value%10].pop(self.table[value%10].index(value))
            else:
                return False


l1=HashTableChaining()
l1.InsertValue(10)
l1.InsertValue(100)
print(l1.HashSearch(10))
print(l1.HashDelete(10))

