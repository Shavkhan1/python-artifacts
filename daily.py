#Day 1: simple To-Do List 
#This program asks the user to input 3 tasks and print them
# tasks = []  # create an empty list

# #Prevents crashes from invalid input
# number_of_tasks = input("How many tasks do you want to add to your To-Do List? ")
# while not number_of_tasks.isdigit() or int(number_of_tasks) <= 0:
#     print("Please enter a valid positive number. ")
#     number_of_tasks = input("How many tasks do you want to add to your To-Do List? ")
# number_of_tasks = int(number_of_tasks)
# for i in range(number_of_tasks):
#     task = input(f"Enter task {i+1}: ")
#     tasks.append(task)  # store each task in the list

# for i, task in enumerate(tasks):
#     print(f"Task {i+1}: {task}")


#Day 2: improved To-Do List

#Day 3: adding saving and loading functionality

#Day 4 IDK wtf I am doing atp

#Day 5: adding task completion status and deletion functionality
# def load_tasks():
#     tasks = []
#     try:
#         with open("tasks.txt", "r") as file:
#             for line in file:
#                 title, done = line.strip().split("|")
#                 tasks.append({
#                     "title": title,
#                     "done": done == "True"
#                 })
#     except FileNotFoundError:
#         pass
#     return tasks


# def save_tasks(tasks):
#     with open("tasks.txt", "w") as file:
#         for task in tasks:
#             file.write(f"{task['title']}|{task['done']}\n")


# def add_tasks(tasks):
#     task_text = input("Enter a new task: ")

#     while task_text.strip() == "":
#         print("Task cannot be empty.")
#         task_text = input("Enter a new task: ")

#     task = {
#         "title": task_text,
#         "done": False
#     }

#     tasks.append(task)


# def show_tasks(tasks):
#     if not tasks:
#         print("Your To-Do List is empty.")
#         return

#     print("Your To-Do List:")
#     for i, task in enumerate(tasks):
#         status = "[x]" if task["done"] else "[ ]"
#         print(f"{status} Task {i + 1}: {task['title']}")


# def mark_task_done(tasks):
#     if not tasks:
#         print("Your To-Do List is empty.")
#         return
#     show_tasks(tasks)

#     task_number = input("Enter the task number to mark as done: ")

#     while not task_number.isdigit() or int(task_number) <= 0 or int(task_number) > len(tasks):
#         print("Please enter a valid task number.")
#         task_number = input("Enter the task number to mark as done: ")

#     task_index = int(task_number) - 1
#     tasks[task_index]["done"] = True
#     print(f"Task {task_number} marked as done.")

# def delete_task(tasks):
#     if not tasks:
#         print("Your To-Do List is empty.")
#         return
#     show_tasks(tasks)

#     task_number = input("Enter the task number to delete: ")

#     while not task_number.isdigit() or int(task_number) <= 0 or int(task_number) > len(tasks):
#         print("Please enter a valid task number.")
#         task_number = input("Enter the task number to delete: ")

#     task_index = int(task_number) - 1
#     deleted_task = tasks.pop(task_index)
#     print(f"Task '{deleted_task['title']}' deleted.")

# def main():
#     tasks = load_tasks()

#     while True:
#         command = input("Command (add/list/done/delete/exit): ").strip().lower()

#         if command == "add":
#             add_tasks(tasks)

#         elif command == "list":
#             show_tasks(tasks)

#         elif command == "exit":
#             save_tasks(tasks)
#             print("Tasks saved. Exiting.")
#             break
#         elif command == "done":
#             mark_task_done(tasks)
#         elif command == "delete":
#             delete_task(tasks)


#         else:
#             print("Unknown command.")


# if __name__ == "__main__":
#     main()

#day 6

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title.strip():
            print("Task cannot be empty.")
            return
        self.tasks.append(Task(title))

    def show_tasks(self):
        if not self.tasks:
            print("Your To-Do List is empty.")
            return
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}: {task}")

    def mark_task_done(self, number):
        if number < 1 or number > len(self.tasks):
            print("Invalid task number.")
            return
        self.tasks[number - 1].mark_done()
        print(f"Task {number} marked as done.")

    def delete_task(self, number):
        if number < 1 or number > len(self.tasks):
            print("Invalid task number.")
            return
        deleted = self.tasks.pop(number - 1)
        print(f"Deleted task: {deleted.title}")

    def save_tasks(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.done}\n")

    def load_tasks(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    title, done = line.strip().split("|")
                    self.tasks.append(Task(title, done == "True"))
        except FileNotFoundError:
            pass
def main():
    todo = ToDoList()
    todo.load_tasks()

    while True:
        command = input("Command (add/list/done/delete/exit): ").strip().lower()

        if command == "add":
            title = input("Enter a new task: ")
            todo.add_task(title)

        elif command == "list":
            todo.show_tasks()

        elif command == "done":
            todo.show_tasks()
            number = input("Enter the task number to mark as done: ")
            if number.isdigit():
                todo.mark_task_done(int(number))

        elif command == "delete":
            todo.show_tasks()
            number = input("Enter the task number to delete: ")
            if number.isdigit():
                todo.delete_task(int(number))

        elif command == "exit":
            todo.save_tasks()
            print("Tasks saved. Exiting.")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()