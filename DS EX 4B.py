class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

def enqueue():
    global front, rear
    car = input("Enter car number to park: ")
    newNode = Node(car)
    if rear is None:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode
    print("Car parked.")

def dequeue():
    global front, rear
    if front is None:
        print("Queue is Empty!")
    else:
        print("Car removed:", front.data)
        temp = front
        front = front.next
        del temp
        if front is None:
            rear = None

def display():
    if front is None:
        print("Queue is Empty!")
    else:
        print("Cars in parking:")
        temp = front
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")

while True:
    print("\nQueue Menu:")
    print("1. Park a Car")
    print("2. Remove a Car")
    print("3. Show All Cars")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice! Try again.")


'''
Queue Menu:
1. Park a Car
2. Remove a Car
3. Show All Cars
4. Exit
Enter choice (1-4): 1
Enter car number to park: Tn720010
Car parked.

Queue Menu:
1. Park a Car
2. Remove a Car
3. Show All Cars
4. Exit
Enter choice (1-4): 1
Enter car number to park: Tn720020
Car parked.

Queue Menu:
1. Park a Car
2. Remove a Car
3. Show All Cars
4. Exit
Enter choice (1-4): 3
Cars in parking:
Tn720010 --> Tn720020 --> NULL

Queue Menu:
1. Park a Car
2. Remove a Car
3. Show All Cars
4. Exit
Enter choice (1-4): 2
Car removed: Tn720010

Queue Menu:
1. Park a Car
2. Remove a Car
3. Show All Cars
4. Exit
Enter choice (1-4): 4
Exiting Program.

'''