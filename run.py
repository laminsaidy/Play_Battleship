# import random package to create random board 
from random import randint


print("Welcome to my Battlefield Game")
print("            Ships ")
print("     0  1  2  3  4  5  6  7  8  9")

hit = [19,20,]
miss = [6,10,22,26]
destroy = [21]
counter = 0 
# create a nested for loop that prints "." in a row and a nested if/else statement to check if ship is hit, miss or destroyed
for x in range(10):
   row = ""
   for y in range(10):
      sym = " . "
      if counter in miss:
         sym = " x "
      elif counter in hit:
         sym = " o "
      elif counter in destroy:
         sym = " @ "

      row = row + sym
      counter = counter + 1
   print(x," ",row)
   
# create a function to get shot input from user
def take_a_shot():
# Create a while loop to check if shot is correct or incorrect
     alright = "no"
     while alright == "no":
         shot = input("place your shot please")#
         shot = int(shot)
         if shot <0 or shot >99:
            print("OOOPS! That's incorrect. Please try again")
         else:
            alright = "yes"
            break
     return shot
shot = take_a_shot()
