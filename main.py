# File-Based To-Do List Application

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid choice!")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
