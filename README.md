# WELCOME TO MY ULTIMATE BATTLESHIPS
Battleship is a strategy type guessing game for two or more players. It allows the user to play on ruled grids on which each user's fleet of ships are marked. The locations of the fleets are concealed from the other user. It allows users to take alternate turns to shoot at each others ships, and the objective of the game is to destroy the opposing user's fleet. My  site’s goal is to provide an easy but challenging game to entertain the Users.

# Rules of the game

- Users can play against the computer on a 10x10 grid board.
- Ships are randomly placed on board and only numbers are allowed.
- Coordinates outside Grid size are not allowed and previous guesses can't be use twice.
- The player and computer take guesses trying to sink each others Battleships.
- Each has ten shots and the first to sink all the opponents ships wins the the game.
<br>

## Site Owner Goals 

- Use the game as part of a portfolio to show what has been learned. 

- Make sure players have a great time playing the game.

- Create features that make players want to keep using the game.

# Existing features
- A welcome message with an input field for users to enter their name.
<br>

![screenshot welcome message](images/Screenshot%20(150).png)

- 10x10 Grid board.
<br>

![screenshot grid board](images/Screenshot%20(151).png)

- If both players misses, it indicates " O ".
<br>

![screenshot "O"](images/Screenshot%20(158).png)

- If player hits a ship, it indicates " P ".
<br>

![screenshot "P"](images/Screenshot%20(157).png)

- If computer hits a ship, it indicates " C ".
<br>

![screenshot "C"](images/Screenshot%20(153).png)

- Only coordinate numbers are allowed.
<br>

![screenshot "only coordinate numbers"](images/Screenshot%20(155).png)

- A number can only be use once.
<br>

![screenshot "Invalid numbers"](images/Screenshot%20(154).png)

- The game ends when a player hits more ships from the opponent.
<br>

![screenshot "End of game"](images/Screenshot%20(156).png)






# Future features
- Ability to play online against another friend.
- More ships and increase board size.
- Real life images to indicate hit, miss or destroyed.
- A game with different ship sizes.
- Ability to change the number of ships and board size.

# Testing

![screenshot "PEP8 Linter"](images/Screenshot%20(160).png)

- The game has been tested through the [PEP8](https://pep8ci.herokuapp.com/#) linter. 

# Technologies Used

- Languages: 
  - Python

- Platform: 
  - Heroku

# Bugs
There was no symbols on the board game when a player take a shot as intended therefore, I had to rewrite the board function properly to get it fixed.
## Remaining Bugs
There are no Bugs remaining.

## Validator testing
### Input validation

- Player cannot guess a coordinate twice or outside the board

![Invalid input, Repeated Coordinate](images/Screenshot%20(154).png)

# Deployment
This project was deployed using the Code Institute's mock terminal for Heroku.

These steps were taken for the deployment:

- Create an account or log in to Heroku.

- On the dashboard, in the right corner click the button that says "New" and choose "Create New App".

- Pick a name of the app. The name has to be unique because it can't match any other name being used.

- Select your region, United States or Europe. 

- "Create App".

- On the menu at the top of the page, go to the Settings Tab.

- Scroll down to Config Vars and click "Reveal Config Vars".

- Add a new Config Var and enter PORT in the keybox and 8000 in the valuebox.

- Under Config Vars you will find Buildpacks. 

- Click "Add Buildpacks".

- Select python.

- Repeat this step but select nodejs. 

- Important to know: The python has to be picked before the nodejs, if it is not you can change the order by click and drag to correct the order. 

- Scroll back to the top of the page, to the menu and go to the Deploy Tab.

- Select GitHub as the deployment method and confirm. 

- Search for you repository name and connect that. 

- Scroll down to the bottom of the page and there you can choose if you want the deploys to be Automatic or Manually. The Manually deployed branches needs redepolying each time the repository is updated. 

- Click "View" to see the live site. 

## Credits
- Wikidipedia for the details on the Battleship game. 
- Youtube videos on how to go by the Project. 
- Code Institute lessons and projects.
- My mentor Moritz for his advice and support.


