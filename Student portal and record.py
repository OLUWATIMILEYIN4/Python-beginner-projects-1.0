"""
STUDENT LOGIN & GRADING PORTAL
Features: 
- Validates username/password length
- Maps department abbreviations (MCE, MEE, etc.)
- Calculates averages and assigns grades
"""

# Your code starts here...

#Student login portal 
username = input('Create a username: ')
if len(username) < 5:
    print('Username too short! Must be at least 5 characters long')
else:
    print('Valid username')
password = input('Create a password: ')
if len(password) < 6:
    print('Password too weak! Must be at least 6 characters long')
else:
    print('Strong password')
department = input("Enter your department's abbreviation in caplocks")
if department == 'MCE':
    print('Mechatronics Engineering')
elif department =='MEE':
    print('Mechanical Engineering')
elif department =='MBBS':
    print('Medicine and surgery')
elif department =='SCIENCE':
    print('Science and technology')
else:
    print('Department not found!')
#name and final stage 
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
university = input("Enter your university's name in full: ")
print(f'Welcome {last_name}, {first_name} to the {university}. We are glad to have you here')
print('Please input your scores in your last exam. Thank you')
maths = int(input('Enter your maths score: '))
physics = int(input('Enter your physics score: '))
chemistry = int(input('Enter your chemistry score: '))
english = int(input('Enter your english score: '))
#grading system
average = (maths + physics + chemistry + english)/4
if average >= 80:
    grade = 'A'
    message = 'Congratulations on your first exam. Keep grinding'
elif average >= 70:
    grade = 'B'
    message = 'You did well, try harder next time'
elif average >= 60:
    grade = 'C'
    message = "This isn't your best, try harder next time"
elif average >= 50:
    grade = 'D'
    message = "Average performance, this isn't your best"
else: 
    grade = 'F'
    message = 'You did poorly, go and study'

#THIS MUST BE OUTSIDE THE IF BLOCK
print('\n---RESULT---')
print(f'Dear {last_name}, {first_name}')
print(f'Average: {average}')
print(f'Grade: {grade}')
print(message)