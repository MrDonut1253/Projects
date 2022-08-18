import random
import time

while True:

    print("--Rock, Paper, Scissors game--")
    choices = ["rock","paper","scissors"]
    print("Your choices are : rock, paper, scissors.")

    computer = None
    player = None
    play_again= None
    score = 0
    computer_score = 0
    YesNo = ["Yes","yes" ,"No", "no"]

    while score < 3 and computer_score < 3:
        computer= None
        computer = random.choice(choices)
        player = None
        while player not in choices:
            print("")
            player = input("rock, paper, or scissors?: ")
        if player == computer:
            print("")
            print("You have chosen: ", player)
            print("The computer has chosen: ", computer)
            print("its a draw!")
        elif player == "rock":
            if computer =="scissors":
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)
                print("You won this round!")
                score += 1
                print("Your score is: ", score)
            if computer == "paper":
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)               
                print("You lost this round!")
                computer_score += 1
        elif player =="paper":
            if computer == "rock":
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)
                print("You won this round!")
                score += 1
                print("Your score is: ", score)    
            if computer == "scissors":    
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)               
                print("You lost this round!")
                computer_score += 1
        elif player == "scissors":
            if computer == "rock":
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)               
                print("You lost this round!")
                computer_score += 1
            if computer == "paper":
                print("")
                print("You have chosen: ", player)
                print("The computer has chosen: ", computer)
                print("You won this round!")
                score += 1
                print("Your score is: ", score)
        continue

    print("")
    if computer_score > score:
        print("You lost the game!")
        print(score,":", computer_score)
    elif score > computer_score:
        print("You win the game!")
        print(score,":", computer_score)

    while play_again not in YesNo:
        play_again = input("Play again? (Yes/No) : ")
    if play_again != "yes" and play_again != "Yes":
        print("")
        break

print("Bye!")
time.sleep(1)
