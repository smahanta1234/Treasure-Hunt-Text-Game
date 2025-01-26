from time import sleep

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
print("Your mission is to find the treasure. Maybe you will make it there")
print("All moves that you can make start with a capital letter. For Example: Left or Right?")
print("** Please note that this game will annoy you with exit statements almost everytime you make a mistake.**")
print("** I just like trolling my players, haha.**")
first_move = input("Your first move. Left or Right? \n")



if first_move=="Right":
    print("You wandered into nothingness. Game Over!")
    exit()

elif first_move=="Left":
    print("You luckily survived four consecutive animal attacks. Your persistence is commendable.")
    print("You reach the shore.")
    second_move = input("Should you Swim for it or Wait? \n")
    if second_move=="Swim":
        print("Attacked by crocodile. Game Over! Womp Womp")
        exit()
    elif second_move!="Swim" and second_move!="Wait":
        print("Please learn how to type. Died of hunger. Game Over!")
        exit()
    elif second_move=="Wait":
        print("Smart choice lad. You arrived safely to a treasure thanks to the boat you built.")
        door = input("You come across three doors. Which door do you choose? Red, Blue or Yellow? \n")
        if door =="Red":
            print("Engulfed in flames! Game Over.")
            exit()
        elif door=="Blue":
            print("A trapdoor opens and you fall into a sharktank where you get no business offers TT. Game Over.")
            exit()
        elif door=="Yellow":
            print("You have a chance at opening the treasure chest you found")
            minigame="You have a chance to open the chest if you can fully complete the challenges."
            print(minigame)
        else:
            print("Failsafe triggered. You died. Oh, and learn how to type")
            exit()
else:
    print("Practice how to type: Left, Right")
    exit()

test_1 = int(input("Enter a number between 100 and 200 \n"))
if (test_1%2)==0 and 100<test_1<200 :
    print("You chose an even number, you have a pure heart and deserve the treasure.")
else:
    sleep(3)
    print("Failsafe triggered. The chest shot out poison darts. You died.")
test_2=(input("Lets test your patience now. Type patience in 2 seconds \n"))
if test_2 == "patience":
    print("You unlocked the chest and got absolutely shafted. Your hopes and dreams were shattered because you got only a singular gold coin.")
if test_2 !="patience":
    print("You were going to get something great, but you had to lose concentration. You died. Please learn how to type.")