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

def LOT(root):
    if(root==None):
        return([])
    final=[]
    s1=[root]

    while(s1):
        k=[]
        for i in range (len(s1)):
            e=s1.pop(0)
            if(e.left):
                s1.append(e.left)
            if(e.right):
                s1.append(e.right)
            k.append(e.data)
        final.append(k)
    return(final)
        
print(LOT(root))