tasks = []
points = []
while True:
    print('\n--- TO DO LIST MANAGER---')
    print('1. Add Task')
    print('2. View Task')
    print('3. Remove last Task')
    print('4. Sort Tasks')
    print('5. Show Highest Priority')
    print('6. Show Lowest Priority')
    print('7. Show Total Points')
    print('8. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        task = input('Enter task: ')
        score = int(input('Enter task points: '))

        tasks.append(task)
        points.append(score)

        print('Task added successfully!')
    elif choice == '2':
        if len(tasks) == 0:
            print('No tasks available')
        else:
            for i in range(len(tasks)):
                print(tasks[i], '-', points[i], 'points')
    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks available')
        else:
            tasks.pop()
            points.pop()
            removed_task = tasks.pop()
            print('Task removed successfully')
            print(tasks)
            print(points)
    elif choice == '4':
        points.sort()
        for i in range(len(tasks)):
            print(tasks[i], '-', points[i], 'points')