
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

def Post(root,final):
    if(root==None):
        return
    Post(root.left,final)
    Post(root.right,final)
    final.append(root.data)
    return(final)

print(Post(root,final=[]))