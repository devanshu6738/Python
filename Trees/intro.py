class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

Root=TreeNode("Rootnode")
Child1=TreeNode("Child1")
Child2=TreeNode("Child2")
Root.children.append(Child1)
Root.children.append(Child2)