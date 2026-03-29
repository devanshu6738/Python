class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def PreOrder(root):
    if root is None:
        return
    print(root.value)
    PreOrder(root.left)
    PreOrder(root.right)

def Inorder(root):
    if root is None:
        return 
    Inorder(root.left)
    print(root.value)
    Inorder(root.right)

def PostOrder(root):
    if root is None:
        return 
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.value)


RootNode=BinaryTree(20)
Child1=BinaryTree(10)
Child2=BinaryTree(30)
RootNode.left=Child1
RootNode.right=Child2
Child3=BinaryTree(45)
Child4=BinaryTree(78)
Child5=BinaryTree(45)

Child1.left=Child3
Child1.right=Child4
Child2.right=Child5

PreOrder(RootNode)
PostOrder(RootNode)
Inorder(RootNode)