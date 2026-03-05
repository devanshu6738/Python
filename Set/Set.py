My_set=set()
My_set.add(2)
My_set.add(3)
print(My_set)


# No duplicate Value

lst=[1,2,2,3,3,3,4,4,4,4]
St2=set(lst)
print(St2)
print(list(set(lst)))

# update Add Multiple element with the iterable(list,tuple,set,,)

s1={1,2,3,4}
s1.update([5,6])
print(s1)

#  remove- Remove the specified element , if its not contain than it will show an error
s1.remove(3)
print(s1)

#discard- Discard the specified element , also if its not contain then it will do not show an error
s1.discard(3)
print(s1)

#pop()- it will randomly removes the element from the set and return the removed value

print(s1.pop())
print(s1.pop())
print(s1.pop())

#  clear - it will delete all the element present in the set

s1.clear()
print(s1)