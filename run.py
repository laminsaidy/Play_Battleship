# import random package to create random board 
from random import randint

# Create a function to get shot input from user
def take_a_shot(total_guesses):
   
# Create a while loop to check if shot is correct or incorrect
     alright = "no"
     while alright == "no":
# Create a try and except method incase of an error to avoid a crash
         try:
            shot = input("place your shot please")
            shot = int(shot)
            if shot <0 or shot >99:
               print("OOOPS! That's incorrect. Please try again")
# Check if player used a recent guess
            elif shot in total_guesses:
               print("That's invalid! It has been used before")
            else:
               alright = "yes"
               break
         except:
               print("That's invalid! Please try again")
         return shot

def board (hit, miss, destroy):
   print("            Ships ")
   print("     0  1  2  3  4  5  6  7  8  9")

   counter = 0
# Create a nested for loop that prints "." in a row and a nested if/else statement to check if ship is hit, miss or destroyed
   for x in range(10):   
       row = ""
       for y in range(9):
         symb = " . "
       if counter in miss:
         symb = " x "
       elif counter in hit:
         symb = " o "
       elif counter in destroy:
         symb = " 0 "

       row = row + symb
       counter = counter + 1
       print(x," ",row*10)


    

#Create a function to validate a shot of hit, miss or destroy Ship
def validate_shot(shot,ship1,ship2,hit,miss,destroy):

# An if statement to validate if it's a hit, miss or on a ship
   if shot in ship1:
      ship1.remove(shot)
      if len(ship1) > 0:
         hit.append(shot)
      else:
         destroy.append(shot)
   elif shot in ship2:
      ship2.remove(shot)
      if len(ship2) > 0:
         hit.append(shot)
      else:
         destroy.append(shot)
   else:
      miss.append(shot)

   return ship1, ship2, hit, miss, destroy

ship1 = [6,16,26]
ship2 = [45,46,47]
hit = []
miss = []
destroy = []  


# Condition for how many shots are allowed
for i in range (10):
   total_guesses = hit + miss + destroy
   ship1, hit, miss, destroy = validate_shot = (ship1, hit, miss, destroy)
   shot = take_a_shot(total_guesses)
   board(hit, miss, destroy)

# Condition to end the Game and break out of a loop
   if len(ship1) < 1 and len(ship2) < 1:
      print("You are the winner")
      break
print("End of Game")







