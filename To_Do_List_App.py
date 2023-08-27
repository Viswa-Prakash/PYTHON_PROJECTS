
## To_Do_List_App.py
tasks = []

def add_task(task):
    tasks.append(task)

def view_task():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}: {task}")

def remove_task():
    tasks.pop()
    

while True:
    print(" 1. Add Task")
    print(" 2. View Task")
    print(" 3. Remove Task")
    print(" 4. Exit Task")

    choice = input ("Enter your choice: ")

    if choice == '1':
        new_task = input("Enter new task: ")
        add_task(new_task)
        print("The task has been added successfully")

    elif choice == '2':
        view_task()
    
    elif choice == '3':
        remove = int(input("Enter task number to remove: "))
        remove-=1
        tasks.pop(remove)
        
        print("The task has been removed successfully")
        
    elif choice == '4':
        print("Bye")
        break

    else:
        print("Invalid choice, Please try again")






