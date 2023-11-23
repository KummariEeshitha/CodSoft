class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def update_task(self, index, new_task):
        if index < len(self.tasks):
            self.tasks[index] = new_task
            print(f"Task at index {index} updated.")
        else:
            print(f"Invalid index {index}.")

    def print_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

todo_list = ToDoList()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Print Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        index = int(input("Enter the index of the task to update: "))
        new_task = input("Enter the new task: ")
        todo_list.update_task(index, new_task)
    elif choice == "3":
        todo_list.print_tasks()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")