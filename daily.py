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

def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()] 
    except FileNotFoundError:
        pass  # If the file doesn't exist, start with an empty list
    return tasks



def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_tasks(tasks):
    task = input("Enter a new task: ")
    while task.strip() == "":
        print("Task cannot be empty. Please enter a valid task.")
        task = input("Enter a new task: ")
    tasks.append(task)

def show_tasks(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
    else:
        print ("Your To-Do List:")
        for i, task in enumerate(tasks):
            print(f"Task {i+1}: {task}")

def main():
    tasks = load_tasks()
    while True:
        command = input("Command (add/list/exit): ").strip().lower()
        if command == "add":
            add_tasks(tasks)
        elif command == "list":
            show_tasks(tasks)
        elif command == "exit":
            save_tasks(tasks)
            print("Tasks saved. Exiting the program.")
            break
        else:
            print("Unknown command. Please enter 'add', 'list', or 'exit'.")



if __name__ == "__main__":
    main()

