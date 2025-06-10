import os

FILENAME = "tasks.txt"

def load_tasks():
    """
    Load tasks from file into a dictionary:
    {id: {"task": description, "done": bool}}
    """
    tasks = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    task_id, task_desc, status = parts
                    tasks[int(task_id)] = {
                        "task": task_desc,
                        "done": (status == "Done")
                    }
    return tasks

def save_tasks(tasks):
    """
    Write tasks to file, formatted as:
    id | description | Done/Pending
    """
    with open(FILENAME, "w") as file:
        for task_id, info in tasks.items():
            status = "Done" if info["done"] else "Pending"
            file.write(f"{task_id} | {info['task']} | {status}\n")

def add_task(tasks):
    """Prompt user and add a new task."""
    desc = input("Enter the task description: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"task": desc, "done": False}
    print(" Task added.")

def delete_task(tasks):
    """Prompt for task ID and remove it."""
    try:
        task_id = int(input("Enter the task ID to delete: "))
        if task_id in tasks:
            del tasks[task_id]
            print(" Task deleted.")
        else:
            print(" Task not found.")
    except ValueError:
        print(" Invalid ID—please enter a number.")

def mark_completed(tasks):
    """Prompt for task ID and mark it as done."""
    try:
        task_id = int(input("Enter the task ID to mark as completed: "))
        if task_id in tasks:
            tasks[task_id]["done"] = True
            print(" Task marked as completed.")
        else:
            print(" Task not found.")
    except ValueError:
        print(" Invalid ID—please enter a number.")

def display_tasks(tasks):
    """Show all tasks with their status."""
    if not tasks:
        print(" No tasks found.")
    else:
        print("\n--- Current Tasks ---")
        for task_id, info in sorted(tasks.items()):
            mark = "Correct" if info["done"] else "Wrong"
            print(f"{task_id}. {info['task']} [{mark}]")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Completed")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_completed(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(" Tasks saved. Goodbye!")
            break
        else:
            print(" Invalid choice; please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
