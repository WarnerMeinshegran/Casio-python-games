# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('_____|_____|_____')
 
    print("  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('_____|_____|_____')
 
    print("  {}  |  {}  |  {}".format(values[6], values[7], values[8]))

# Function to print the score-board
def print_scoreboard(score_board):
    print("SCOREBOARD")
    players = list(score_board.keys())
    print("", players[0], "", score_board[players[0]])
    print("", players[1], "", score_board[players[1]])
    input("Press EXE\nto continue")
    
 
# Function to check if any player has won
def check_win(player_pos, cur_player):
 
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(cur_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Player", cur_player, "turn\nWhich box?", end="")
            move = int(input()) 
        except ValueError:
            input("Wrong Input\nOnly numbers\npress EXE\nto continue")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            input("Wrong Input\n1-9 only!\npress EXE\nto continue")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            input("Place already filled\nTry again\npress EXE\nto continue")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("\nPlayer ", cur_player, " has won")     
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Draw")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

print("Original ver:\nwww.askpython.com/\npython/examples/\ntic-tac-toe\n-using-python\nadapted to calc\nby Hamza")
try:
    gm=int(input)('''
    Gamemode:
    1=Player vs AI
    2=Player vs Player
    Choose gamemode:''')
    if gm > 2:
        raise ValueError
except ValueError:
    print("Only numbers 1 and 2")
player1 = input("Plr1 name:")
if gm==2:
    player2="AI"
else:    
    player2 = input("Plr2 name:")

# Stores the player who chooses X and O
cur_player = player1

# Stores the choice of players
player_choice = {'X' : "", 'O' : ""}

# Stores the options
options = ['X', 'O']

# Stores the scoreboard
score_board = {player1: 0, player2: 0}
print_scoreboard(score_board)

# Game Loop for a series of Tic Tac Toe
# The loop runs until the players quit 
while True:

    # Player choice Menu
    print("\nTurn to choose for\n", cur_player)
    print("Enter 1 for X")
    print("Enter 2 for O")
    print("Enter 3 to Quit")

    # Try exception for CHOICE input
    try:
        choice = int(input())   
    except ValueError:
        print("Wrong input\nOnly numbers.\nPress EXE\nto continue")
        continue

    # Conditions for player choice  
    if choice == 1:
        player_choice['X'] = cur_player
        if cur_player == player1:
            player_choice['O'] = player2
        else:
            player_choice['O'] = player1

    elif choice == 2:
        player_choice['O'] = cur_player
        if cur_player == player1:
            player_choice['X'] = player2
        else:
            player_choice['X'] = player1
        
    elif choice == 3:
        print("Final Scores")
        print_scoreboard(score_board)
        break  

    else:
        print("Wrong input\nnumbers 1-3 only\nPress EXE\nto continue")

    # Stores the winner in a single game of Tic Tac Toe
    winner = single_game(options[choice-1])
        
    # Edits the scoreboard according to the winner
    if winner != 'D' :
        player_won = player_choice[winner]
        score_board[player_won] = score_board[player_won] + 1

    print_scoreboard(score_board)
    # Switch player who chooses X or O
    if cur_player == player1:
        cur_player = player2
    else:
        cur_player = player1
# by
# https://www.askpython.com/python/examples/tic-tac-toe-using-python
# Adapted to casio fx-9860giii calculator by blabla_lab