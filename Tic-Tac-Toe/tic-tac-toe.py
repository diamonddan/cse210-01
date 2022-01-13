'''Daniel McNary
1/13/2022
CSE 210 Programming With Classes

Your program must also meet the following requirements.

1.The program must have a comment with assignment and author names.
2.The program must have at least one if/then block.
3.The program must have at least one while loop.
4.The program must have more than one function.
5.The program must have a function called main.'''

#-------Global Variables-----------#

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
#If game is still going
game_still_going = True
#Who won? Or Tie?
winner = None
#Whos turn is it?
current_player = "X"


def main():

  display_board()

  while game_still_going:
   handle_turn(current_player)
    #Check if the game has ended
   check_if_game_over()
    #Flip to the other player
   flip_player()
   #The game has ended
   if winner == "X" or winner == "O":
    print(winner + " won.")
   elif winner == None:
        print("Tie.")
  


#Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print('--+---+--')
  print(board[3] + " | " + board[4] + " | " + board[5])
  print('--+---+--')
  print(board[6] + " | " + board[7] + " | " + board[8])

#Handle a single turn of player
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1-9: ")
  position = int(position) - 1

  board[position] = player

  display_board()


def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():
    #Setup global variables
    global winner

    #Check Rows
    row_winner = check_rows()
    #Check Columns
    column_winner = check_columns()
    #Check Diagonals
    diag_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_rows():
    #Set up global variable
    global game_still_going
    #Check if any of the rows have value and not empty
    row_1 = board[0] ==  board[1] == board[2] != "-"
    row_2 = board[3] ==  board[4] == board[5] != "-"
    row_3 = board[6] ==  board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    #Set up global variable
    global game_still_going
    #Check if any of the rows have value and not empty
    column_1 = board[0] ==  board[3] == board[6] != "-"
    column_2 = board[1] ==  board[4] == board[7] != "-"
    column_3 = board[2] ==  board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner (X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    #Set up global variable
    global game_still_going
    #Check if any of the rows have value and not empty
    diag_1 = board[0] ==  board[4] == board[8] != "-"
    diag_2 = board[6] ==  board[4] == board[2] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    #Return the winner (X or O)
    if diag_1:
        return board[0]
    if diag_2:
        return board[6]
    return




if __name__ == "__main__":
    main()