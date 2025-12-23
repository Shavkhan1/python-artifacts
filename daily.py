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
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()] 
    except FileNotFoundError:
        pass  # If the file doesn't exist, start with an empty list
    return tasks

def add_tasks(tasks):
    
    while True:
        task = input("Enter a task (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        if task.strip() == "":   # check for empty input
            print("You entered an empty task. Please enter a valid task.")
            continue
        if task.startswith("&") or task.endswith(".py"):
            print("That doesn't look like a task.")
            continue

        tasks.append(task)

def show_tasks(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
    else:
        print ("Your To-Do List:")
        for i, task in enumerate(tasks):
            print(f"Task {i+1}: {task}")

tasks = load_tasks()
add_tasks(tasks)
show_tasks(tasks)
save_tasks(tasks)


