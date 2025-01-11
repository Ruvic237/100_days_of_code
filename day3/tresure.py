#Tresure island Game
print("Welcome to tresure Island.\nYour mission is to find the tresure. ")

message = {
            "blue":"GameOver!! because Room is full of beasts",
            "red":"GameOver!! because Room is full of Fire",
            "yellow":"Woupii you have won!! the Room is full of arms and good souls"
        }

#store user direction 
direction = input("You're at a cross road. where do you want to go (left,right)? ").lower()

#make sure user gives correct input
while direction not in ["left","right"]:
    direction = input("wrong input try again right or left ?").lower()

#determine if user will stop the game now
if direction == "right":
    print("GameOver.. You fell into a hole")
else:    
    #user wish to swim or wait base on situation?(swim=gover)
    user_action = input("There is an island in the middle of the lake (swim or wait) for boat? ").lower()
    
    #check if user stop here or continue
    if user_action == "swim":
        print("GameOver you are drawn")
    else:            
        #which door user choose to safe him self based on the color of the door
        user_color = input("You arrived unharmed.This house has 3 doors of diff colors.Choose your's (red,yellow or blue)? ").lower()
        result = message[user_color]
        
        #check if user enters correct color
        while user_color not in ["red","yellow","blue"]:
            user_color = input("Wrong input write correct color ").lower()
            
        #determine if user wins or lose
          
        # if user_color == "blue" or user_color == "red":
        #     print(f"{result} ")
        # else:
        #     print(f"{result} ")   
         
        print(result)
   