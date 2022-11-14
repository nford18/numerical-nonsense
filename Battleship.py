from random import randint
from math import ceil

def print_board(board):
  for row in board:
    print("  ".join(row))
def generate_ship(board):
  row = randint(0, len(board) - 1)
  col = randint(0, len(board[0]) - 1)
  return [row,col]

board = []
size = int(input("Board Size: "))
for x in range(size):
  board.append(["O"] * size)
ships = []
num_ships = int(ceil(size/3))
for i in range(num_ships):
  ships.append(generate_ship(board))
print("There are", num_ships, "ships on the board")
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
turn = 0
sink_count = 0
while (turn < 4):
  print("Turn", turn+1)
  print_board(board)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  is_hit = False
  for ship in ships:
    if(guess_row == ship[0] and guess_col == ship[1]):
      is_hit = True
      break
  if is_hit:
    is_hit = False
    print("You hit one of my ships!")
    board[guess_row][guess_col] = "W"
    sink_count +=1
    if(sink_count == num_ships):
      print("Congratulations! You sunk all my battleships!")
      break
  else:
    if (guess_row < 0 or guess_row > size-1) or (guess_col < 0 or guess_col > size-1):
      print("Oops, that's not even in the ocean.")
      
    elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "W"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      turn += 1
    if(turn == 4):
      print("Game Over")