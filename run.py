# Import random package to create random board

from random import randint

player_hits = []
player_misses = []
computer_hits = []
computer_misses = []
player_ship = [6, 16, 26]
computer_ship = [45, 46, 47]

print("Welcome to Battleship!")
player1_name = input("Please enter your name: ")
print(f"Hello {player1_name}! Let's get it on.")


def board():
    print("            Ships ")
    print("     0  1  2  3  4  5  6  7  8  9")

    counter = 0
    for x in range(10):
        row = ""
        for y in range(10):
            symb = " . "
            if counter in player_misses or counter in computer_misses:
                symb = " O "
            elif counter in player_hits:
                symb = " P "
            elif counter in computer_hits:
                symb = " C "
            row += symb
            counter += 1
        print(x, " ", row)


def takeAShot(total_guesses):
    alright = False
    while not alright:
        try:
            shot = input("Place your shot please: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("OOOPS! That's incorrect. Please try again.")
            elif shot in total_guesses:
                print("That's invalid! It has been used before.")
            else:
                alright = True
        except ValueError:
            print("That's invalid! Please try again.")
    return shot


def computerShot(total_guesses):
    shot = randint(0, 99)
    while shot in total_guesses:
        shot = randint(0, 99)
    return shot


def validateShotPlayer(shot):
    global player_ship
    if shot in player_ship:
        player_ship.remove(shot)
        player_hits.append(shot)
    else:
        player_misses.append(shot)


def validateShotComputer(shot):
    global computer_ship
    if shot in computer_ship:
        computer_ship.remove(shot)
        computer_hits.append(shot)
    else:
        computer_misses.append(shot)


for i in range(20):
    total_guesses_player = player_hits + player_misses
    total_guesses_computer = computer_hits + computer_misses
    board()

    # Player's turn

    shot = takeAShot(total_guesses_player)
    validateShotPlayer(shot)

    # Computer's turn

    shot = computerShot(total_guesses_computer)
    validateShotComputer(shot)

    print(f"Computer shot at position {shot}")

    # Condition to end the Game and break out of a loop

    if not player_ship:
        print("You are the winner!")
        break
    elif not computer_ship:
        print("Computer is the winner!")
        break
else:
    print("End of Game")
