def add_task(task_name):
    todo_list.append(task_name)

def view_all_tasks():
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")

def mark_task_as_completed(task_name):
    if task_name in todo_list:
        todo_list.remove(task_name)
        completed_tasks.append(task_name)
    else:
        print("The task is not found in the list.")

def view_all_completed_tasks():
    for i, task in enumerate(completed_tasks):
        print(f"{i+1}. {task}")

todo_list = []
completed_tasks = []

while True:
    print("\nPlease chose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")

    user_input = input("User Input: ")

    if user_input == "1":
        task_name = input("Enter the task: ")
        add_task(task_name)
        print(f"The task “{task_name}” was added to the todo list")
    elif user_input == "2":
        view_all_tasks()
    elif user_input == "3":
        task_name = input("Enter the name of the task: ")
        mark_task_as_completed(task_name)
        print(f"The task {task_name} is marked as completed")
    elif user_input == "4":
        view_all_completed_tasks()
    elif user_input == "5":
        break
    else:
        print("Invalid input, please try again.")

