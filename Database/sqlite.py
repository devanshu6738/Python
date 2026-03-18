import sqlite3
conn=sqlite3.connect("Database.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
               id int,
               name text,
               experience int,
               location text
               )
""")

# Inserting a Data

cursor.execute("""
INSERT INTO Employee VALUES
(2,'Devanshu Gupta',2,'India'),
(1,'Ayush',3,'India')
""")

# List all the Employee

result=cursor.execute("SELECT * FROM Employee")
lst_result=[]
for row in result:
    print(row) 
    lst_result.append(row)


print(lst_result)

import pandas as pd

df=pd.DataFrame(lst_result,columns=["id","name","experience","location"])
print(df.head())
df.to_csv("Employee.csv",index=False)
