import json

# Initialize tasks list
tasks = []

# Load tasks from a JSON file if it exists
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task():
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = int(input("Enter priority (1 - low, 2 - medium, 3 - high): "))
    task = {
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    tasks.sort(key=lambda x: (x["completed"], x["priority"], x["due_date"]))
    print("Task List:")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{idx}. Title: {task['title']} | Due Date: {task['due_date']} | Priority: {task['priority']} | Status: {status}")

# Function to mark a task as complete
def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter the number of the task to mark as complete: ")) - 1

    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_number = int(input("Enter the number of the task to delete: ")) - 1

    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    tasks.extend(load_tasks())

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

