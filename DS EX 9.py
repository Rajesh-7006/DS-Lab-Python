class Node:
    def __init__(self, enrollment_id, student_name):
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1

        return y

    def _insert(self, node, enrollment_id, student_name):
        if not node:
            return Node(enrollment_id, student_name)

        if enrollment_id < node.enrollment_id:
            node.left = self._insert(node.left, enrollment_id, student_name)
        elif enrollment_id > node.enrollment_id:
            node.right = self._insert(node.right, enrollment_id, student_name)
        else:
            # Duplicate IDs are not allowed
            return node

        # Update height of this ancestor node
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Get balance factor
        balance = self._balance_factor(node)

        # If node becomes unbalanced, then 4 cases

        # Left Left Case
        if balance > 1 and enrollment_id < node.left.enrollment_id:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and enrollment_id > node.right.enrollment_id:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and enrollment_id > node.left.enrollment_id:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and enrollment_id < node.right.enrollment_id:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def insert(self, enrollment_id, student_name):
        self.root = self._insert(self.root, enrollment_id, student_name)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, enrollment_id):
        if not node:
            return node

        if enrollment_id < node.enrollment_id:
            node.left = self._delete(node.left, enrollment_id)
        elif enrollment_id > node.enrollment_id:
            node.right = self._delete(node.right, enrollment_id)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            temp = self._min_value_node(node.right)
            node.enrollment_id = temp.enrollment_id
            node.student_name = temp.student_name
            node.right = self._delete(node.right, temp.enrollment_id)

        if not node:
            return node

        # Update height
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Get balance factor
        balance = self._balance_factor(node)

        # Balance the node if unbalanced

        # Left Left Case
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, enrollment_id):
        self.root = self._delete(self.root, enrollment_id)

    def _search(self, node, enrollment_id):
        if not node or node.enrollment_id == enrollment_id:
            return node
        if enrollment_id < node.enrollment_id:
            return self._search(node.left, enrollment_id)
        return self._search(node.right, enrollment_id)

    def search(self, enrollment_id):
        result = self._search(self.root, enrollment_id)
        if result:
            return f"Enrollment ID: {result.enrollment_id}, Student Name: {result.student_name}"
        else:
            return "Enrollment record not found."

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [(node.enrollment_id, node.student_name)] + self._inorder(node.right)

    def inorder_traversal(self):
        return self._inorder(self.root)

    def count_enrollments(self):
        return self._count(self.root)

    def _count(self, node):
        if not node:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)


def manage_enrollments():
    tree = AVLTree()
    while True:
        print("\n--- Student Enrollment Management ---")
        print("1. Insert Enrollment Record")
        print("2. Delete Enrollment Record by ID")
        print("3. Search Enrollment Record by ID")
        print("4. Traverse All Enrollments (Inorder)")
        print("5. Count Total Enrollments")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            enrollment_id = int(input("Enter Enrollment ID: "))
            student_name = input("Enter Student Name: ")
            tree.insert(enrollment_id, student_name)
            print(f"Student {student_name} with ID {enrollment_id} enrolled.")

        elif choice == '2':
            enrollment_id = int(input("Enter Enrollment ID to delete: "))
            tree.delete(enrollment_id)
            print(f"Enrollment with ID {enrollment_id} deleted.")

        elif choice == '3':
            enrollment_id = int(input("Enter Enrollment ID to search: "))
            result = tree.search(enrollment_id)
            print(result)

        elif choice == '4':
            enrollments = tree.inorder_traversal()
            if enrollments:
                print("\nSorted Enrollments (by Enrollment ID):")
                for enrollment in enrollments:
                    print(f"Enrollment ID: {enrollment[0]}, Student Name: {enrollment[1]}")
            else:
                print("No enrollment records found.")

        elif choice == '5':
            total_enrollments = tree.count_enrollments()
            print(f"Total Enrollments: {total_enrollments}")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    manage_enrollments()
