# Set Operation

a={1,2,3}
b={2,3,4}

# Union - it will return all the element present in the set
print(a.union(b))
print(a|b)

# Intersection - it will return all the common element in the set
print(a.intersection(b))
print(a & b)

# Difference - return the element which is in the first set but not in the second set
print(a.difference(b))
print(a-b)

# symmetric_difference -> it will return the element that are either of the sets but not both
print(a.symmetric_difference(b))
print(a^b)


# issubset -> it will check the element of the set is in the other set
a={1,2,3,4}
b={1,2,3,4,5,6}
print(a.issubset(b))

# issuperset ->
print(b.issuperset(a))

# isdisjoint
a={1,2,3,4}
b={5,6,7,8}
print(a.isdisjoint(b))