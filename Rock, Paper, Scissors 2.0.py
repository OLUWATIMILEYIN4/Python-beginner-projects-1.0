"""This is a new rock, paper scissors
game that has some intellgence 
I did this but giving it the ability 
to analyze your past moves and
predict your future moves ensuring 
its victory"""
import random

choices = ["rock", "paper", "scissors"]

player_history = []

player_score = 0
computer_score = 0

difficulty = input("Choose difficulty: easy, medium, hard: ").lower()
while True:
    
    user = input("\nRock, Paper, Scissors (or quit): ").lower()

    if user == "quit":
        print("Game Over")
        break
    if user not in choices:
        print('Invalid choice!')
        continue 
    player_history.append(user)
    rock_count = player_history.count("rock")
    paper_count = player_history.count('paper')
    scissors_count = player_history.count('scissors')
    if rock_count >= paper_count and rock_count >= scissors_count:
        predicted = "rock"
    elif paper_count >= rock_count and scissors_count:
        predicted = 'paper'
    else:
        predicted = 'scissors'
        #---- Counter move ----
    if predicted == "rock":
        smart_choice = "paper"
    elif predicted == 'paper':
        smart_choice = 'scissors'
    else:
        smart_choice = 'rock'
        #---- Difficulty System ----
    if difficulty == "easy":
        computer = random.choice(choices)
    elif difficulty == "medium":
        if random.randint(1, 2) == 1:
            computer = random.choice(choices)
        else:
            computer = smart_choice
    else: #Hard
        computer = smart_choice
    print("You chose:", user)
    print("Computer chose:", computer)
    
    if user == computer:
        print("Draw")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1
        
    print("Score -> Player:", player_score, "Computer:", computer_score)