my_dict={"key1":"val1","key2":"val2"}
print(my_dict)

person={
    "name":"Devanshu",
    "age":21,
    "is_student":True,
    "skill":["Python","Cpp","Web_dev"]
}

print(person)

marks=dict()
marks["Devanshu"]=92
print(marks)

marks={
    "Devanshu":92,
    "Dragon":99,
    "Ved":"100"
}
print(marks)
print(marks.keys())

# iteration over dict keys

for key in marks:
    print(key)

#  it can also convert into other types

print(list(marks.keys()))
print(tuple(marks.keys()))

print(marks.values())
for value in marks:
    print(value)

print(marks["Devanshu"])

#  get method

print(person.get("name"))  
print(person.get("id",-1))   # if the key is not present in the dictionary so its will return the value in the parameter of the get method 

#  Removing the element 
print(my_dict.pop("key1"))
print(my_dict)

print(person.popitem())  # remove and return the last enter key value pair in dictionary

print(my_dict.clear())

animal={}
animal["fly"]="eagle"
animal["land"]="tiger"
print(animal)

# Nesting Dictionary 
xyz={
    "key1":"value1",
    "nestkey":{
        "key2":"val2",
        "key3":"val3"
    }
}

print(xyz["nestkey"]["key3"])

# Checking Membership
print("name" in person.keys())
print("Devanshu" in person.values())


# Dictionary Comprehension

my_dic2={}

for i in range(10):
    my_dic2[i]=i*i

print(my_dic2)


my_dic2={i:i*i for i in range(10)}
print(my_dic2)