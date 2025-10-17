def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    print("Enter student marks separated by space:")
    marks_str = input().strip()
    marks = list(map(float, marks_str.split()))  

    bubble_sort(marks)

    print("\nMarks sorted in ascending order:")
    print(" ".join(f"{mark:.2f}" for mark in marks))

if __name__ == "__main__":
    main()
