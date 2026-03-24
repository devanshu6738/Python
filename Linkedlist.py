
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

        
    
    def InsertAtBeginning(self,data):
        next_node=Node(data)
        next_node.next=self.head
        self.head=next_node
        print(next_node.data)

    def InsertAtEnd(self,data):
        next_node=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=next_node
        print(temp.next.data)

    def InsertAtIndex(self,index,data):
        next_node=Node(data)
        count=0
        temp=self.head
        prev=None
        while count!=index:
            count+=1
            prev=temp
            temp=temp.next
        prev.next=next_node
        next_node.next=temp    

    def deleteAtBegining(self):
        self.head=self.head.next
        
    def deleteAtIndex(self,index):
        temp=self.head
        prev=None
        count=0
        while count!=index:
            count+=1
            prev=temp
            temp=temp.next
        prev.next=temp.next



    def search(self,key):
        temp=self.head
        while temp!=None:
            if temp.data==key:
                return True
            temp=temp.next
        return False

l1=Linkedlist()
l1.InsertAtBeginning(10)
l1.InsertAtEnd(20)
l1.InsertAtEnd(30)
l1.InsertAtEnd(40)
l1.display()
l1.InsertAtIndex(2,60)
l1.display()
print(l1.search(60))
print(l1.search(90))
l1.deleteAtBegining()
l1.display()
l1.InsertAtIndex(3,70)
l1.display()
l1.deleteAtIndex(3)
l1.display()

# finally linked list implementation done :-)

