print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input('you are at the cross of the road . where do you want to go ? Type "left" or "right" ? ')

if road == "left":
    print("you won the 2nd round and now you can swim or you can choose to wait !")
    choice =input('you have to come to a lake . There is an island in the middle of the lake.'
                   'Type "wait" to wait for a boat . Type "swim" to swim across  ').lower()

    if choice == "wait":
        choice1 = input("you arrive at the island unharmed . There is the house with 3 doors . "
                        "one red , one blue , one yellow . "
                        "Which colour do you want to choose  ").lower()
        if choice1 == "red":
            print("it is a room of fire so you loose . Play again sometimes !")
        elif choice1 == "blue":
            print("it is a room of water so you loose  . Play again sometimes !")
        elif choice1 == "yellow":
            print("you choose the right path so you can go ahead . Congratulation for winning the treasure !")
        else:
            print("you choose the wrong colour! so try again .")

    else:
        print("you got attacked by an angry trout . Game over !")

else:
    print(" you fell into a hole . game over !")


