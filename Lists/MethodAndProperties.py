#list[start:stop:step]   slicing

lst=[21,34,56,56,78,90]

print(lst[1])
print(lst[0])

print(lst[0:5:2])   #slicing

#Concantenation  -- its does not affect original list 

lst1=["Devanshu","Two"]

print(lst1+["Never Give Up"]) 
print(lst1)


#Basic Methods-

lst2=[43,54,89,56,32,70]

#Append
lst2.append('append me')  #inplace
print(lst2)

#Pop
lst2.pop()
print(lst2)

#Sorting And Reverse in List
lst2.reverse()
print(lst2)

lst2.sort()
print(lst2)

lst3=['d','e','v','a','n','s','h','u']
lst3.sort()
print(lst3)

#Nesting List

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
matrix=[l1,l2,l3]
print(matrix)

print(matrix[0])
print(matrix[0][1])


#List Comprehensions
val=[]
for i in range(5):
    val.append(i)

print(val)

val=[i for i in range(10)]
print(val)

#Problem: from matrix List extract the first column data.
print(matrix)

first_col=[row[0] for row in matrix]
print(first_col)


#Count
val=[1,2,3,4,5,6]
print(val.count(2))

#Extend

val.extend([1,2])
print(val)

# what is difference between append and extend

val.append([1,2])
print(val)

# index - item with the value 2 example (if the number is not present in the list is will so the error) 

print(val.index(2))  

#insert in list - list_name.insert(index,object)

val.insert(2,"Devanshu")
print(val)

# remove in list

val.remove("Devanshu")
print(val)