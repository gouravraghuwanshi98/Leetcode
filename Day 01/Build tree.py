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

print(root.right.left.data)

