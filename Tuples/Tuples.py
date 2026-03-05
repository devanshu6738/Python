#  what is tuples?
#  basically tuples is just like a list its have a both hetrogeneous and homogeneous data but the tuples is Immutable , ordered 
# Allow Duplicate
# Support Indexing and Slicing 
# Faster than list

t1=(1,2,3,4,5)
print(t1)  #homogeneous

t2=(2,"Devanshu",True)
print(t2) #hetrogeneous

# indexing

print(t2[1])
print(t1[0])
print(t2[-1])


# Slicing
# tuple(start:end:Jump)
print(t2[1:])
print(t1[::2])

# reverse trick

print(t2[::-1])