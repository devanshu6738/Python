# Structured arrays in NumPy are homogeneous at the array level (each element has the same layout).
# We can specify a type and, optionally, a name on a per-column basis. This makes sorting and filtering even more powerful, and it can feel similar to working with data in Excel, CSVs, or relational databases.
import numpy as np

record=[
        ("Devanshu",21,92),
        ("Ayush",21,94),
        ("Dev",20,90)
]
arr=np.array(record,dtype=[("name","U15"),("age",np.int32),("Marks",np.int32)])
print(arr)
print(arr[0])