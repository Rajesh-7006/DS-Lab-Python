class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        newNode = Node(value)
        if self.rear is None:
            self.front = self.rear = newNode
            print(f"Car {value} entered the parking lot.")
        else:
            self.rear.next = newNode
            self.rear = newNode
            print(f"Car {value} entered the parking lot.")

    def dequeue(self):
        if self.front is None:
            print("Parking lot is empty! No cars to leave.")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Car {temp.data} left the parking lot.")

    def display(self):
        if self.front is None:
            print("Parking lot is empty!")
            return
        temp = self.front
        print("Cars currently in parking lot:")
        while temp:
            print(f"{temp.data} ---> ", end="")
            temp = temp.next
        print("NULL")

if __name__ == "__main__":
    q = Queue()
    while True:
        print("\n--- Car Parking System ---")
        print("1. Car Entry (Enqueue)")
        print("2. Car Exit (Dequeue)")
        print("3. Display Parking Lot")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            car = input("Enter Car Number: ")
            q.enqueue(car)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting... Traffic system closed.")
            break
        else:
            print("Invalid choice! Try again.")
