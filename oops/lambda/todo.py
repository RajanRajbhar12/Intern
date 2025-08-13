tasks=[]

while True:
    print("1: Enter a task")
    print("2: View tasks")
    print("3: Delete a task")
    print("4: Exit")
    
    choice = input("Enter a choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")