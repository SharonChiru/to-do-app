# todo.py

import os

def load_tasks():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def mark_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index] = f'[X] {tasks[index]}'
        save_tasks(tasks)
        print(f'Task {index + 1} marked as completed.')
    else:
        print('Invalid task index.')

def display_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
    else:
        print('No tasks found.')

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f'Task "{deleted_task}" deleted.')
    else:
        print('Invalid task index.')

def main():
    while True:
        print('\nTodo List:')
        print('1. Add Task')
        print('2. Mark Task as Completed')
        print('3. Display Tasks')
        print('4. Delete Task')
        print('5. Quit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter task: ')
            add_task(task)
        elif choice == '2':
            index = int(input('Enter task index to mark as completed: ')) - 1
            mark_completed(index)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            index = int(input('Enter task index to delete: ')) - 1
            delete_task(index)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()

# todo.py

import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# ... (rest of the code remains unchanged)

if __name__ == "__main__":
    main()
