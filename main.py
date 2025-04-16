import json
import os

filename = "tasks.json"

def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []

def add_task():
    title = input("Podaj treść zadania: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    print()
    print("Twoje zadania: ")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def mark_task_done():
    show_tasks()
    selected = int(input("Które zadanie odhaczyć?: "))
    if 0 < selected <= len(tasks):
        tasks[selected - 1]["done"] = True
    show_tasks()
    save_tasks(tasks)

def delete_task():
    show_tasks()
    selected = int(input("Które zadanie usunąć?: "))
    if 0 < selected <= len(tasks):
        del tasks[selected - 1]
    else:
        print("Nieprawidłowy numer zadania.")

    save_tasks(tasks)
    print("Zadanie usunięte.")

def edit_task():
    show_tasks()
    selected = int(input("Które zadanie chcesz edytować: ")) - 1
    if 0 <= selected < len(tasks):
        new_title = input("Podaj nową treść zadania: ")
        if new_title.strip() == "":
            print("Nie można ustawić pustej treści.")
        else:
            tasks[selected]["title"] = new_title
    else:
        print("Nieprawidłowy numer zadania.")
    
    save_tasks(tasks)
    print("Zadanie zostało zaktualizowane.")

    
tasks = load_tasks()

while True:
    print()
    print("Wybierz opcję: ")
    print("1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Oznacz jako wykonane")
    print("4. Usuń zadanie")
    print("5. Edytuj zadanie")
    print("6. Wyjdź")
    print()

    wybór = int(input("Twój wybór: "))

    if wybór == 1:
        add_task()
    elif wybór == 2:
        show_tasks()
    elif wybór == 3:
        mark_task_done()
    elif wybór == 4:
        delete_task()
    elif wybór == 5:
        edit_task()
    elif wybór == 6:
        break
    else:
        print("Nieprrawidłowy wybór, spróbuj ponownie.")