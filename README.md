# WELCOME TO MY ULTIMATE BATTLESHIPS
Battleship is a strategy type guessing game for two players. It is played on ruled grids on which each player's fleet of ships are marked. The locations of the fleets are concealed from the other player. Players take alternate turns to shoot at the other player's ships, and the objective of the game is to destroy the opposing player's fleet. My  site’s goal is to provide an easy but challenging game to entertain the Users.
#### How to play
This is a Python Battleship game for two players (you against the computer). 

The game begins with a welcome message and the player is asked to enter their name
![screenshot welcome message](images/Screenshot%20(150).png)

The player and computer take guesses trying to sink each others Battleships.

If both players misses, it indicates " O ".

If player hits a ship, it indicates " P ".

If computer hits a ship, it indicates " C ".

Each has ten shots and the first to sink all the opponents ships wins the the game. 
# Existing features
Player enters their name. <br>
You play against computer. <br>
Accepts user input. <br>
Ships are randomly placed on board. <br>
Grid: Play on a 10x10 board. <br>
Coordinates outside Grid size are not allowed. <br>
Only numbers are allowed. <br>
Previous guesses can't be use twice.

### Future features
Multiple players. <br>
More ships and increase board size. <br>
Real life images to indicate hit, miss or destroyed. <br>

# Testing
I have manually tested the code through my local terminal and the codeinstitute Heroku terminal. <br>
Tested the code through CI Python Linter validator and no errors where found.


# Bugs
There was no symbols on the board game when a player take a shot as intended therefore, I had to rewrite the board function properly to get it fixed.
### Remaining Bugs
There are no Bugs remaining.
### Validator testing
No errors where found on the CI Python Linter validator.

# Deployment
This project was deployed using Codeinstute's mock terminal for Heroku.
## Steps for deployment
Fork or clone this repository. <br>
Create a new Heroku app. <br>
Set the buildbacks to python and NodJS in that order. <br>
Link the Heroku app to the repository. <br>
click on Deploy.

### Credits
Code Institute for the deployment terminal. <br>
Wikidipedia for the details on the Battleship game. <br>
Youtube videos on how to go by the Project. 

