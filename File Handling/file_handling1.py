f=open("sample.txt",'w')
f.write("""Python is an interpreted high-level general-purpose programming language.
File handling is an important part of many web and desktop applications.
This sample text file contains multiple lines of data for testing.
You can read, write, append, and search terms within this file.
End of the file record.
""")
f.close()

# f.write()--> since file is closed hence this method not work

# write multiple strings
f=open("sample1.txt",'w')
f.write('hello world')
f.write('\n Let code in Python')
f.close()

# if the file is already present

f=open("sample.txt",'w')
f.write('\n python is luv')
f.close()

f=open("sample1.txt",'a')   #append mode
f.write("\n i m fine")
f.close()


L=['hello\n','hi\n','how are you ?\n','I am fine\n']
f=open("sample.txt",'w')
f.writelines(L)
f.close()


# using read

f=open('sample.txt','r')
s=f.read()
print(s)
f.close()

f=open("sample.txt")
s=f.read(10)
print(s)
f.close()


#  readline() --> to read line by line

f=open("sample.txt")
print(f.readline(),end='')
print(f.readline(),end='')
f.close()

# reading entire line using readline

f=open("sample.txt")
while f.readline() !='':
    print(f.readline(),end='')
    
f.close()