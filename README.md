# WELCOME TO MY ULTIMATE BATTLESHIPS
Battleship is a strategy type guessing game for two or more players. It allows the user to play on ruled grids on which each user's fleet of ships are marked. The locations of the fleets are concealed from the other user. It allows users to take alternate turns to shoot at each others ships, and the objective of the game is to destroy the opposing user's fleet. My  site’s goal is to provide an easy but challenging game to entertain the Users.

# Rules of the game

<li>Users can play against the computer on a 10x10 grid board</li>
<li>Ships are randomly placed on board and only numbers are allowed.</li>
<li>Coordinates outside Grid size are not allowed and previous guesses can't be use twice</li>
<li>The player and computer take guesses trying to sink each others Battleships.</li>
<li>Each has ten shots and the first to sink all the opponents ships wins the the game.</li>
<br>

# Existing features
<li>A welcome message with an input field for users to enter their name</li>

![screenshot welcome message](images/Screenshot%20(150).png)

<li>10x10 Grid board</li>

![screenshot grid board](images/Screenshot%20(151).png)

<li>If both players misses, it indicates " O ".</li>

![screenshot "O"](images/Screenshot%20(158).png)

<li>If player hits a ship, it indicates " P ".</li>

![screenshot "P"](images/Screenshot%20(157).png)

<li>If computer hits a ship, it indicates " C ".</li>

![screenshot "C"](images/Screenshot%20(153).png)

<li>Only coordinate numbers are allowed</li>

![screenshot "only coordinate numbers"](images/Screenshot%20(155).png)

<li>A number can only be use once</li>

![screenshot "Invalid numbers"](images/Screenshot%20(154).png)

<li>The game ends when a player hits more ships from the opponent</li>

![screenshot "End of game"](images/Screenshot%20(156).png)






# Future features
<li>Ability to play online against another friend.</li>
<li>More ships and increase board size.</li>
<li>Real life images to indicate hit, miss or destroyed.</li>
<li>A game with different ship sizes</li>
<li>Ability to change the number of ships and board size</li>
<br>

# Testing
I have manually tested the code through my local terminal and the codeinstitute Heroku terminal. <br>
Tested the code through CI Python Linter validator and no errors where found.


# Bugs
There was no symbols on the board game when a player take a shot as intended therefore, I had to rewrite the board function properly to get it fixed.
## Remaining Bugs
There are no Bugs remaining.
## Validator testing
No errors where found on the CI Python Linter validator.

# Deployment
This project was deployed using Codeinstute's mock terminal for Heroku.
## Steps for deployment
Fork or clone this repository. <br>
Create a new Heroku app. <br>
Set the buildbacks to python and NodJS in that order. <br>
Link the Heroku app to the repository. <br>
click on Deploy.

## Credits
Code Institute for the deployment terminal. <br>
Wikidipedia for the details on the Battleship game. <br>
Youtube videos on how to go by the Project. 

