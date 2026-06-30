integer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    user = input('Create a password: ')
    if len(user) > 8 and any(char in user for char in integer):
        print('Strong Password')
        break
    else:
        print('Weak PASSWORD must be at least 8 characters long and contain a number!')