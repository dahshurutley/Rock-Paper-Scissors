import random
import time
import sys

itemList = ("Rock", "Paper", "Scissors")
B = random.choice(itemList)
print(B)
user_input= input("Please Select Rock, Paper, Or Scissors (Case Sensitive!): ")
guess = 0
if user_input not in itemList:
    print("Please Restart the Program, and Enter one of The Correct Choices!")
    sys.exit()

time.sleep(2)





if user_input == B:
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        time.sleep(1.8)
        print("It's a Tie!")

elif user_input == "Paper":
    if B == "Rock":
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        time.sleep(1.8)
        print("You Won!")
    else: 
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        print("You Lost")

elif user_input == "Rock":
    if B == "Scissors":
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        time.sleep(1.8)
        print("You Won!")
    else: 
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        print("You Lost")


elif user_input == "Scissors":
    if B == "Paper":
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        time.sleep(1.8)
        print("You Won!")
    else: 
        print(f"You chose {user_input}, The Computer Chose {B} \n")
        print("You Lost")

input('Press ENTER to exit')


    





