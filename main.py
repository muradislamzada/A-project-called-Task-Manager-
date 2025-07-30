import json
from task import Task
tasks = []
def load_tasks():
    try:
        with open("tasks.json", "r") as name1:
            data = json.load(name1)
            for i in data:
                task = Task(i["Title"], i["Description"])
                tasks.append(task)
    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.json", "w") as name1:
        json.dump([j.to_dict() for j in tasks], name1)
def add_task():
    title = input("Task name: ")
    desc = input("Task description: ")
    task = Task(title, desc)
    tasks.append(task)
    save_tasks()
    print("Task added!")
def show_tasks():
    if not tasks:
        print("There is no task.")
        return
    for l, task in enumerate(tasks, start=1):
        print(f"{l}. {task.title} - {task.description}")
load_tasks()
while True:
    print("\n1. Add task\n2. Show tasks\n3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        save_tasks()
        break
    else:
        print("Wrong choice.")