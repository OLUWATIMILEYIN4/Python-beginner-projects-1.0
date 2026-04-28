import random

choices = ["rock", "paper", "scissors"]
while True:
    user = input('Enter rock, paper, or scissors: ').lower()
    if user in choices:
        break
    else:
        print('Invalid choice! Try again') 
        
print('You chose:',user)
    
#Computer choice
computer = random.choice(choices)
print("Computer chose:", computer)
#game logic
if user == computer:
    print("it's a draw")
elif user == 'rock' and computer == 'scissors':
    print('You win!')
elif user == 'paper' and computer == 'rock':
    print('You win!')
elif user == 'scissors' and computer == 'paper':
    print('You win!')
else:
    print('You lose!')