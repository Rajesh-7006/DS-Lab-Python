def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def main():
    print("Enter registered student roll numbers separated by space:")
    registered_str = input().strip()
    registered = list(map(int, registered_str.split()))

    roll_number = int(input("Enter roll number to search for: "))

    found_linear = linear_search(registered, roll_number)

    registered_sorted = sorted(registered)
    print("\nSorted roll numbers for binary search:", registered_sorted)
    found_binary = binary_search(registered_sorted, roll_number)

    print("\nLinear Search:")
    if found_linear:
        print(f"Roll number {roll_number} is registered.")
    else:
        print(f"Roll number {roll_number} is NOT registered.")

    print("\nBinary Search:")
    if found_binary:
        print(f"Roll number {roll_number} is registered.")
    else:
        print(f"Roll number {roll_number} is NOT registered.")

if __name__ == "__main__":
    main()
