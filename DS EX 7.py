class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
print("||---> BINARY TREE IMPLEMENTATION <---||")
root = None
values=[]
rn=int(input("Enter the No.of Elemets : "))
for i in range(rn):
    v = int(input("Enter The Numbers ---> "))
    values.append(v)
for val in values:
    root = insert(root, val)
print("\nInorder Traversal   (Left → Root → Right):")
inorder(root)
print("\n\nPreorder Traversal  (Root → Left → Right):")
preorder(root)
print("\n\nPostorder Traversal (Left → Right → Root):")
postorder(root)
print()
