with open("sample.txt",'w') as f:
    f.write("selmon kon")
    
with open("sample.txt") as f:
    print(f.read())

    
with open("sample1.txt") as f:
    print(f.read(10))
    print(f.read(10))
    
big_L=['hello_world!' for i in range(1000)]

with open("sample.txt",'w') as f:
    f.writelines(big_L)
    
    
with open("sample.txt",'r') as f:
    chunk_size=10
    
    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end='***')
        f.read(chunk_size)

print('\n')
        
# seek and tell
with open("sample1.txt",'r') as f:
    print(f.read(10))
    print(f.tell())
    print(f.seek(0))
    print(f.read(10))