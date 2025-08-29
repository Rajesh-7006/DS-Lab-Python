SIZE=5
queue=[None]*SIZE
front=-1
rear=-1
def enqueue(value):
    global rear,front
    if rear==SIZE-1:
        print("Queue is Full! Insertion is not possible")
    else:
        if front==-1:
            front=0
        rear+=1
        queue[rear]=value
        print(f"{value} enque to dequeue")
def dequeue():
    global rear,front
    if front==-1 or front>rear:
        print("Queue is EMPTY! Cannot dequeue.")
    else:
        removed=queue[front]
        print("f{removed}dequeued from the queue.")
        front+=1
        if front>rear:
            front=rear=-1
def display():
    if front==-1 or front>rear:
        print("Queue is empty!")
    else:
        print("Queue elements are:")
        for i in range (front,rear+1):
            print(queue[i])
while True:
    print("\n---Queue Operations Menu")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    choice=input("Enter your choice(1-4):")
    if choice == '1':
       value = input("Enter value to enqueue: ")
       enqueue(value)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
