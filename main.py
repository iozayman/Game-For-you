print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

q1 = input('There is a town nearby, do you want to "teleport" or just "walk"?').lower()
a = 0
q6 = 0
if q1 == "walk":
  q2 = input("You are an idiot but lucky enough to survive. Do you want to ride the horse? (Y/N)\n").lower()
  if q2 == "y":
    q3 = input('Horse is safer way to travel boi. But the horse is stolen from a barbar. He wants to know "Who are you?" to forgive you. \nHINT: Confuse him\n').lower()
    if q3 == "you":
      q4 =input("You win!").lower()
      if q4 == "you win!":
        q5 = input("No. You win!").lower()
        q6 = "creepy mf. you win"
        if q5 == "no. you win!":
          while a== 0:
            if q6 == "creepy mf. you win":
              q6 = 0
              q6 = input("Creepy MF. YOU WIN").lower
          else:
            a += 1
            print("You cant challenge the computer. DIE")
        else:
          print("DIE")
      else:
        print("You cant steal from barbars MUAHAHAHAHA")
          
    else: 
      print("Slow one dies. GAME OVER FAT ASS")
  else:
    print("horses are agressive. Game over")
else:
  print("Something went wrong. You burn. Game over.")





