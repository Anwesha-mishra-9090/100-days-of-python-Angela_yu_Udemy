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

game_image  = [rock,paper,scissors]

user_choice = int(input("what do you choose ? Type 0 for Rock, 1 for paper or 2 for scissors. \n"))
# 0 ,1 ,2
if user_choice >= 0 and user_choice <= 2:
   2
   print(game_image[user_choice])

computer_choice = random.randint(0,2)
print(f"computer choose :")
print(game_image[computer_choice])
if  user_choice  == 1 and computer_choice == 0:
    print("you win!")
elif user_choice >= 3 or computer_choice <= 0:
   print("invalid number!")
elif user_choice == 0 and computer_choice == 2:
    print("you wins!")
elif user_choice == 0 and computer_choice == 0 :
    print("draw!")

elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you loose !")
elif user_choice > computer_choice:
    print("you win !")
elif computer_choice == user_choice:
    print("draw!")

