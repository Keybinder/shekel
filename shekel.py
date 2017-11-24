import re

f_mov_input = re.compile("[a-gA-G][1-8] [a-gA-G][1-8]")
turnw = True

piece_to_bin_dict = {
     '.' : 0b000,
     'S' : 0b010,
     'W' : 0b100,
     'X' : 0b110,
     's' : 0b011,
     'w' : 0b101,
     'x' : 0b111
}

#blank_board = [['.' for x in range(8)] for x in range(7)] #why is this needed?

# ------------------------------------------------------------------------------

def set_board(in_board_f="boardstart.txt"):
     with open(in_board_f) as f:
          in_board = f.read()
     # TODO: Run basic checks on file before using it as board
     in_board = in_board.split("\n")
     main_board = []
     for i in in_board:
          main_board.append(list(i))
     return main_board

# ------------------------------------------------------------------------------

def parse_move(usr_move):

     # This function parses a move in the format that a user would provide;
     # it returns an array of four values as array references to the board if
     # the move is valid and returns None otherwise.
     
     # PLEASE NOTE THAT array references are given in the order such that the
     # row comes first and the column comes second i.e. opposite order that
     # the user would input. This should make assigning values to main board
     # straightforward.
     
     usr_move = usr_move.strip()
     
     if re.match(f_mov_input, usr_move):
         move_out = []
         usr_move = usr_move.split()
         for i in usr_move:
              for j in list(i):
                   move_out.append(j)

         for x in [0,2]:
              move_out[x] = int(ord(move_out[x].lower())) - int(ord('a'))
         for x in [1,3]:
              move_out[x] = 7 - (int(move_out[x]) - 1) # bit of a hack but works

         for x in [0,2]:
              move_out[x], move_out[x+1] = move_out[x+1], move_out[x]
         
         return move_out
         
     else:
         return None

# ------------------------------------------------------------------------------

##def display_board(board, x=1, y=0, gridref=True, compact=False): #add colours? orientation
##
##     gridnums = [i for i in range(8,0,-1)]
##     gridletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
##     
##     for i in range(8):
##          if gridref == True:
##               line = str(gridnums[i]) + "|"
##          elif gridref == False:
##               line = ""
##          
##          for j in board[i]:
##               line = line + (x * ' ') + j
##          if gridref == False or y == 0:
##               print(line + (y * '\n'))
##          else:
##               print(line + (y * '\n |'))
##               # pretty sure this shouldn't work but it does
##          
##     if gridref == True:
##          print((" +") + ('-' * (7 + 7 * x)))
##          lastline = "  "
##          for i in gridletters:
##               lastline = lastline + (x * ' ') + i
##          print(lastline)
##
##     if compact == False:
##          print('')

# ------------------------------------------------------------------------------

def is_legal_move(move, board):
     # TODO: Complete this function
     
     s1, s2, f1, f2 = move
     legal_move = True
     start_square = board[s1][s2]
     fin_square = board[f1][f2]
     stdpiece = start_square.lower()

     if start_square == '.':
          legal_move = False
     elif turnw != start_square.isupper():
          legal_move = False
     elif fin_square != '.':
          legal_move = False
          
     # Check if moving square is within range of piece VVV
     elif stdpiece == 's' and not (s2 == f2 and f1 == s1-1):
          legal_move = False
     elif stdpiece == 'w' and not (abs(f1-s1) == abs(f2-s2) == 1):
          legal_move = False
     elif stdpiece == 'x' and not (2 > abs(f1-s1) >= 0 and 2 > abs(f2-s2) >= 0):
          legal_move = False
          
     # TODO: Check if piece could be captured
     return legal_move

# ------------------------------------------------------------------------------

def move_piece(move, board): # Returns board after piece has been moved
     s1, s2, f1, f2 = move
     board1 = board
     if is_legal_move(move, board) == True:
          board1[f1][f2] = board[s1][s2]
          board1[s1][s2] = '.'
     return board1     

# ------------------------------------------------------------------------------

##def menu():
##     print(startup_msg)
##     # TODO: Add actual menu with user input and option selection
     
# ------------------------------------------------------------------------------

# Testing below
##shekel_board = set_board()
##
##display_board(shekel_board)
##
###display_board(shekel_board, x=0, y=0)
###display_board(shekel_board, gridref=False)
###display_board(shekel_board, x=2, y=2)
###display_board(shekel_board, x=0, y=1)
##
##menu()
##
##while True:
##     user_in = input('> ')
##     if parse_move(user_in) != None:
##          move = parse_move(user_in)
##          s1, s2, f1, f2 = move
##          print(shekel_board[s1][s2])
##          print(shekel_board[f1][f2])
##          print(is_legal_move(move, shekel_board))
##          shekel_board = move_piece(parse_move(user_in), shekel_board)
##          display_board(shekel_board)
##     else:
##          print("Try Again.")
