import time
import random
import sys

gameOperator = ["rock", "paper", "scissors"]

def rps():
    
    userInput = input("Please Enter Rock, Paper, or Scissors!: ").lower()
    computerChoice = random.choice(gameOperator)
    time.sleep(2)

    if userInput not in gameOperator:
            print("Please Enter one of the Three Choices!\n")

    elif userInput == computerChoice:
        print(f"You chose {userInput}. The Computer Chose {computerChoice}")
        print("It's a Tie!\n")

    elif userInput == "scissors":
        
        if computerChoice == "Rock":
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Lose!\n")

        else:
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Won!\n")
          
    elif userInput == "rock":

        if computerChoice == "paper":
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Lose!\n")

        else:
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Won!\n")
   
    elif userInput == "paper":

        if computerChoice == "rock":
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Won!\n")

        else:
            print(f"You chose {userInput}. The Computer Chose {computerChoice}")
            print("You Lose!\n")

    def restart():

            a = input("Do you want to restart the program? Y/N: ").capitalize()

            if a == "Y":
                rps()

            if a == "N":
                print("Closing Program!...")
                time.sleep(1)
                sys.exit()

            else: 
                print("Unregistered Response? Closing Program...")
                time.sleep(1)
                sys.exit()

    restart()

rps()
