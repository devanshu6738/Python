stack=[]

def push(data):
    stack.append(data)

def pop():
    if len(stack)>0:
        return stack.pop()

def Top():
    if len(stack)>0:
        return stack[-1]
    
def isEmpty():
    return len(stack)==0

def size():
    return len(stack)


push(20)
push(30)
push(40)
push(50)
print(Top())
print(isEmpty())
print(size())
print(pop())

# Stack implementation done :-)

