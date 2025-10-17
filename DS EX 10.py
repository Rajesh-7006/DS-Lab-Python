import heapq

jobs = []

def insert_job():
    name = input("Enter job name: ")
    priority = int(input("Enter job priority: "))
    heapq.heappush(jobs, (priority, name))
    print(f"Added job '{name}' with priority {priority}\n")

def delete_highest():
    if not jobs:
        print("No jobs to delete.\n")
        return
    p, n = heapq.heappop(jobs)
    print(f"Deleted highest priority job '{n}' with priority {p}\n")

def peek_highest():
    if not jobs:
        print("No jobs available.\n")
        return
    p, n = jobs[0]
    print(f"Highest priority job: '{n}' with priority {p}\n")

def display_jobs():
    if not jobs:
        print("No jobs to display.\n")
        return
    print("Jobs in heap order (by priority):")
    for p, n in jobs:
        print(f"Job: {n}, Priority: {p}")
    print()

# ---------- MAIN PROGRAM ----------
while True:
    print("===== Job Scheduler Menu =====")
    print("1. Insert a job")
    print("2. Delete highest priority job")
    print("3. Peek highest priority job")
    print("4. Display all jobs")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        insert_job()
    elif choice == '2':
        delete_highest()
    elif choice == '3':
        peek_highest()
    elif choice == '4':
        display_jobs()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
