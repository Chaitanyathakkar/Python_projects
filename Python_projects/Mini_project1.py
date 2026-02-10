
# ================ Number Guessing Game ===============

import random

target = random.randint(1, 100)

while True:
    UserChoice = input("Guess The Target or Quit: ")
    if (UserChoice == "Quit"):
        break

    UserChoice = int(UserChoice)
    if(UserChoice == target):
        print("Success : Correct Guess!!")
        break

    elif(UserChoice < target ):
        print("Your number was too small. Take a bigger Guess...")
    else:
        print("Your number was too big. Take a smaller Guess...")

print("-----GAME OVER-----")