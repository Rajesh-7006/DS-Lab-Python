SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

def enqueue():
    global rear, front
    if rear == SIZE - 1:
        print("Queue is FULL!!! Insertion is not possible!!!")
    else:
        car = input("Enter the car number to park: ")
        rear += 1
        queue[rear] = car
        if front == -1:
            front = 0
        print("Car parked successfully.")

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue is EMPTY!!!")
    else:
        print("Car removed:", queue[front])
        front += 1
        if front > rear:
            front = -1
            rear = -1

def show():
    if front == -1 or front > rear:
        print("Queue is EMPTY!!!")
    else:
        print("Cars in parking:")
        for i in range(front, rear + 1):
            print(queue[i])

def size():
    if front == -1 or front > rear:
        print("Number of cars in queue: 0")
    else:
        print("Number of cars in queue:", rear - front + 1)

# Main program
while True:
    print("\nQUEUE MENU")
    print("1. Park a Car (Enqueue)")
    print("2. Remove a Car (Dequeue)")
    print("3. Show Cars")
    print("4. Show Queue Size")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        show()
    elif choice == '4':
        size()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

'''

QUEUE MENU
1. Park a Car (Enqueue)
2. Remove a Car (Dequeue)
3. Show Cars
4. Show Queue Size
5. Exit
Enter your choice (1-5): 1
Enter the car number to park: TN72001
Car parked successfully.
QUEUE MENU
1. Park a Car (Enqueue)
2. Remove a Car (Dequeue)
3. Show Cars
4. Show Queue Size
5. Exit
Enter your choice (1-5): 1
Enter the car number to park: TN72002
Car parked successfully.
QUEUE MENU
1. Park a Car (Enqueue)
2. Remove a Car (Dequeue)
3. Show Cars
4. Show Queue Size
5. Exit
Enter your choice (1-5): 3
Cars in parking:
TN72001
TN72002
QUEUE MENU
1. Park a Car (Enqueue)
2. Remove a Car (Dequeue)
3. Show Cars
4. Show Queue Size
5. Exit
Enter your choice (1-5): 4
Number of cars in queue: 2
QUEUE MENU
1. Park a Car (Enqueue)
2. Remove a Car (Dequeue)
3. Show Cars
4. Show Queue Size
5. Exit
Enter your choice (1-5): 2
Car removed: TN72001
'''