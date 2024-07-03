
# import random package to create random board 
from random import randint

hit = []
miss = []
destroy = [] 
ships = [[6,16,26],[45,46,47]]    

print("Welcome to Battleship!")
player1_name = input("Please enter your name: ")
print(f"Hello {player1_name}! Let's get it on.")

def board ():
   # prints gameboard 
   print("            Ships ")
   print("     0  1  2  3  4  5  6  7  8  9")

   counter = 0
# Create a nested for loop that prints "." in a row and a nested if/else statement to check if ship is hit, miss or destroyed
   for x in range(10):   
      row = ""
      for y in range(10):
         symb = " . "
         if counter in miss:
            symb = " o "
         elif counter in hit:
            symb = " x "
         elif counter in destroy:
            symb = " 0 "

         row = row + symb
         counter = counter + 1
      print(x," ",row)


# Create a function to get shot input from user
def take_a_shot(total_guesses):
   
# Create a while loop to check if shot is correct or incorrect
      alright = False
      while not alright:
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
               alright = True
         except:
            print("That's invalid! Please try again")
      return shot



def validate_shot(shot):
   global ships
   is_hit = False
# An if statement to validate if it's a hit, miss or on a ship
   for ship in ships:
      if shot in ship:
         ship.remove(shot)
         hit.append(shot)
         is_hit = True
         if not ship:  # If ship is completely destroyed
            destroy.append(ship)
            ships.remove(ship)
         break
   if not is_hit:
      miss.append(shot)





# Condition for how many shots are allowed
for i in range (10):
   total_guesses = hit + miss + destroy
   board()
   shot = take_a_shot(total_guesses)
   validate_shot(shot)

 
   
  
# Condition to end the Game and break out of a loop
   if len(ships) < 1:
      print("You are the winner")
      break
print("End of Game")