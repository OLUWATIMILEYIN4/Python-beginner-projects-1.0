tasks = []

#Function to show tasks
def show_tasks():
    if len (tasks) == 0:
        print('No tasks available.')
    else:
        print('\nYour Tasks: ')
        for i in range(len(tasks)):
            print(i + 1, '-', tasks[i])

#Function to add tasks 
def add_task():
    task = input('Enter a task: ')
    tasks.append(task)
    print('Task added Successfully.')

#FUNCTION TO REMOVE TASKS
def remove_task():
    show_tasks()
    if len(tasks) > 0:
        number = int(input('Enter the task number to be removed: '))
        removed = tasks.pop(number - 1)
        print(removed, 'was removed.')

#Function to sort tasks
def sort_task():
    tasks.sort()
    print('Tasks sorted alphabetically!')

#Function to count tasks
def count_task():
    print('Total tasks', len(tasks))

#Main program
while True:
    print('\n---TO-DO LIST MANAGER---')
    print('1. Show Tasks')
    print('2. Add Task')
    print('3. Remove Task')
    print('4. Sort Tasks')
    print('5. Count Tasks')
    print('6.Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        sort_task()
    elif choice == '5':
        count_task()
    elif choice == '6':
        print('Sayonara')
        break

    else:
        print('Invalid Choice')