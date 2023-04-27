
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
root=Node(10)
root.left=Node(9)
root.right=Node(8)
root.left.left=Node(7)
root.right.left=Node(6)
root.left.right=Node(11)
root.left.right.left=Node(15)


def H(root):
    if(root==None):
        return(0)
    
    l=H(root.left)
    r=H(root.right)

    return(1+max(l,r))

print(H(root))