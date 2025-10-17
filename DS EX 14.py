class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
    
    def __str__(self):
        return f"Roll No: {self.roll_number}, Name: {self.name}"

class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, student):
        index = student.roll_number % self.size
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index].roll_number == student.roll_number:
                print("Duplicate roll number. Entry not added.")
                return
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full. Cannot insert.")
                return
        
        self.table[index] = student

    def search(self, roll_number):
        index = roll_number % self.size
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index].roll_number == roll_number:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def display(self):
        for i, student in enumerate(self.table):
            print(f"Index {i}: {student if student else 'Empty'}")

class HashTableQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, student):
        index = student.roll_number % self.size
        i = 0
        
        while self.table[(index + i * i) % self.size] is not None:
            new_index = (index + i * i) % self.size
            if self.table[new_index].roll_number == student.roll_number:
                print("Duplicate roll number. Entry not added.")
                return
            i += 1
            if i == self.size:
                print("Hash table is full. Cannot insert.")
                return
        
        self.table[(index + i * i) % self.size] = student

    def search(self, roll_number):
        index = roll_number % self.size
        i = 0
        
        while i < self.size:
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return None
            if self.table[new_index].roll_number == roll_number:
                return self.table[new_index]
            i += 1
        
        return None

    def display(self):
        for i, student in enumerate(self.table):
            print(f"Index {i}: {student if student else 'Empty'}")

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, student):
        index = student.roll_number % self.size
        
        for s in self.table[index]:
            if s.roll_number == student.roll_number:
                print("Duplicate roll number. Entry not added.")
                return
        
        self.table[index].append(student)

    def search(self, roll_number):
        index = roll_number % self.size
        
        for student in self.table[index]:
            if student.roll_number == roll_number:
                return student
        return None

    def display(self):
        for i, students in enumerate(self.table):
            if students:
                print(f"Index {i}: {[str(s) for s in students]}")
            else:
                print(f"Index {i}: Empty")

def main():
    size = int(input("Enter hash table size: "))
    print("Choose collision handling method:")
    print("1. Linear Probing")
    print("2. Quadratic Probing")
    print("3. Chaining")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ht = HashTableLinearProbing(size)
    elif choice == 2:
        ht = HashTableQuadraticProbing(size)
    elif choice == 3:
        ht = HashTableChaining(size)
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Search student")
        print("3. Display table")
        print("4. Exit")
        opt = int(input("Enter option: "))

        if opt == 1:
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            student = Student(roll, name)
            ht.insert(student)

        elif opt == 2:
            roll = int(input("Enter roll number to search: "))
            result = ht.search(roll)
            if result:
                print("Student found:", result)
            else:
                print("Student not found.")

        elif opt == 3:
            ht.display()

        elif opt == 4:
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
