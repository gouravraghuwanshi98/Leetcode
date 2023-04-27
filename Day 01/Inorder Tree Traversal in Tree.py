
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

def LOT(root,l):
    if(root==None):
        return([])
    
    LOT(root.left,l)
    l.append(root.data)
    #print(l)
    LOT(root.right,l)

    return(l)

l=[]
print(LOT(root,l))