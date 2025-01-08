# day4 : Randomization and Python Lists.
#Rock Paper Scissors Game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options= [rock, paper, scissors]

humanchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if humanchoice < 0 or humanchoice >2 :
    print("You Typed invalid number, You Lose!")
else:
    print(options[humanchoice])

print("computer chose:")
computerchoice = random.randint(0,2)
print(options[computerchoice])

if humanchoice >= 0 and humanchoice <= 2:
    if humanchoice == 0 and computerchoice == 2:
        print("You Win!")
    elif humanchoice == 2 and computerchoice == 0:
        print("You Lose!")
    elif humanchoice > computerchoice:
        print("You Win!")
    elif humanchoice < computerchoice:
        print("You Lose!")
    elif humanchoice == computerchoice:
        print("it's a draw")
