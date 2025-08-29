stack = []
MAX = 5
top = -1
def push(book):
    global top
    if top == MAX - 1:
        print("Stack is full, cannot add more books.")
    else:
        top += 1
        stack.append(book)
        print("Book added:", book)
def pop():
    global top
    if top == -1:
        print("Stack is empty. Cannot remove book.")
    else:
        removed_book = stack[top]
        stack.pop()
        top -= 1
        print("Book removed:", removed_book)
def peek():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Top book is:", stack[top])
while True:
    print("\n1. Push book")
    print("2. Pop book")
    print("3. Peek the top book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the book name: ")
        push(title)
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
'''
O/P:

1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 1
Enter the book name: Python
Book added: Python
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 1
Enter the book name: Java
Book added: Java
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 1
Enter the book name: C
Book added: C
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 3
Top book is: C
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 2
Book removed: C
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 3
Top book is: Java
1. Push book
2. Pop book
3. Peek the top book
4. Exit
Enter your choice: 4
'''