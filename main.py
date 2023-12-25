#===========================================================================================
#   Author: Mela Bamiji.
#   Date: 25th December, 2023.
#   
#   Rock, Paper, Scissors Game. An implementation of the popular game written in Python.
#   
#===========================================================================================

import random 

while True:
    # collection of choices 
    choices = ["rock", "paper", "scissors"] 

    # initialize computer's choice and player
    computer = random.choice(choices)   
    player = None

    # prompt player for a choice
    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    # tie: computer and player choice are the same
    if player == computer:
        print("computer: ", computer) 
        print("player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!") 

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!") 

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!") 
    
    # ask user to play again
    play_again = input("Play again? (yes/no): ").lower() 

    if play_again != "yes":
        break 

print("Goodbye!")