#Day 1: simple To-Do List 
#This program asks the user to input 3 tasks and print them
tasks = []  # create an empty list

#Prevents crashes from invalid input
number_of_tasks = input("How many tasks do you want to add to your To-Do List? ")
while not number_of_tasks.isdigit() or int(number_of_tasks) <= 0:
    print("Please enter a valid positive number. ")
    number_of_tasks = input("How many tasks do you want to add to your To-Do List? ")
number_of_tasks = int(number_of_tasks)
for i in range(number_of_tasks):
    task = input(f"Enter task {i+1}: ")
    tasks.append(task)  # store each task in the list

for i, task in enumerate(tasks):
    print(f"Task {i+1}: {task}")
