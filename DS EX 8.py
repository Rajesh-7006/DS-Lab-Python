class LogEntry:
    def __init__(self, entry_time, visitor_name):
        self.entry_time = entry_time
        self.visitor_name = visitor_name

    def __str__(self):
        return f"Time: {self.entry_time}, Visitor: {self.visitor_name}"


class Node:
    def __init__(self, log_entry):
        self.log_entry = log_entry
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, key):
        self.root = None
        self.key = key  # 'time' or 'visitor_name'

    def _compare(self, a, b):
        # Helper comparison function: returns -1 if a < b, 0 if a == b, 1 if a > b
        return (a > b) - (a < b)

    def insert(self, log_entry):
        def _insert(root, log_entry):
            if not root:
                return Node(log_entry)
            cmp = self._compare(log_entry.entry_time, root.log_entry.entry_time)
            if cmp < 0:
                root.left = _insert(root.left, log_entry)
            elif cmp > 0:
                root.right = _insert(root.right, log_entry)
            else:
                print("Duplicate entry based on key, insertion skipped.")
            return root

        self.root = _insert(self.root, log_entry)

    def search(self, key_value):
        def _search(root, key_value):
            if not root:
                return None
            cmp = self._compare(key_value, root.log_entry.entry_time)
            if cmp == 0:
                return root.log_entry
            elif cmp < 0:
                return _search(root.left, key_value)
            else:
                return _search(root.right, key_value)

        return _search(self.root, key_value)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, key_value):
        def _delete(root, key_value):
            if not root:
                return root

            if self.key == 'time':
                cmp = self._compare(key_value, root.log_entry.entry_time)
            else:
                cmp = self._compare(key_value, root.log_entry.visitor_name)

            if cmp < 0:
                root.left = _delete(root.left, key_value)
            elif cmp > 0:
                root.right = _delete(root.right, key_value)
            else:
                # Node with only one child or no child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                # Node with two children:
                temp = self._min_value_node(root.right)
                root.log_entry = temp.log_entry
                # Delete the inorder successor
                key_to_delete = temp.log_entry.entry_time if self.key == 'time' else temp.log_entry.visitor_name
                root.right = _delete(root.right, key_to_delete)
            return root

        self.root = _delete(self.root, key_value)

    def traverse(self):
        result = []

        def _inorder(root):
            if root:
                _inorder(root.left)
                result.append(str(root.log_entry))
                _inorder(root.right)

        _inorder(self.root)
        return result

    def count(self):
        def _count(root):
            if not root:
                return 0
            return 1 + _count(root.left) + _count(root.right)

        return _count(self.root)


def main():
    key = 'time'  # Can be changed to 'visitor_name' if needed
    bst = BinarySearchTree(key)

    while True:
        print("\nMenu:")
        print("1. Insert log entry")
        print("2. Delete log entry")
        print("3. Search log entry")
        print("4. Traverse log entries")
        print("5. Count total entries")
        print("6. Exit")
        option = input("Choose an option: ")

        if option == '1':
            entry_time = input("Enter entry time (e.g., 2025-10-06 14:30): ")
            visitor_name = input("Enter visitor name: ")
            bst.insert(LogEntry(entry_time, visitor_name))
            print("Entry inserted.")

        elif option == '2':
            key_value = input(f"Enter the {key} of the entry to delete: ")
            bst.delete(key_value)
            print("Entry deleted if it existed.")

        elif option == '3':
            key_value = input(f"Enter the {key} to search: ")
            found = bst.search(key_value)
            if found:
                print("Entry found:", found)
            else:
                print("Entry not found.")

        elif option == '4':
            entries = bst.traverse()
            if entries:
                print("Log Entries:")
                for e in entries:
                    print(e)
            else:
                print("No entries found.")

        elif option == '5':
            print(f"Total entries: {bst.count()}")

        elif option == '6':
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
