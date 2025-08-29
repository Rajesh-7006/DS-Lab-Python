class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, title):
        new_node = Node(title)
        new_node.next = self.top
        self.top = new_node
        print("Pushed:", title)

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            temp = self.top
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")
stack = Stack()
stack.push("Java")
stack.push("Python")
stack.display()
stack.pop()
stack.display()

'''
Pushed: Java
Pushed: Python
Python -> Java -> NULL
Popped: Python
Java -> NULL

'''