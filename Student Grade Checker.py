user = int(input('Enter your score: '))
if user >= 70:
    print('Grade: A')
    message = 'Excellent'
    print(message)
elif user >= 60:
    print('Grade: B')
    message = 'Very good'
    print(message)
elif user >= 50:
    print('Grade: C')
    message = 'Good'
    print(message)
elif user >= 40:
    print('Grade: D')
    message = 'Fair'
    print(message)
else:
    print('Grade: F')
    message = 'Fail'
    print(message)
