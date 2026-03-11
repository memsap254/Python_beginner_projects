tasks = []

task1 = input("Enter a task: ")
tasks.append(task1)

task2 = input("Enter another task: ")
tasks.append(task2)

print("Your tasks are:")
for task in tasks:
    print("-", task)