#This code prints out the order that cards are distributed
#to players based on who is the first player out of five
#players

#Imports the random module needed for the code
import random

#The variable, which represents the first player, that
#is set to a random number generator
playerOne = random.randint(1,5)

#The code that runs based on the value assigned to
#playerOne 
if playerOne == 1:
    print("If Player " + str(playerOne) + " is the first ", end="")
    print("player, then the cards are dealt in this order: 1, 2, 3, 4, 5")
else:
    print("If Player " + str(playerOne) + " is the first ", end="")
    print("player, then the cards are dealt in this order: ", end="")
    for num in range(playerOne,6):
        print(num,end=" ")
    for num in range(1, playerOne):
        print(num, end=" ")
 
        
    
    

            
                
            
    