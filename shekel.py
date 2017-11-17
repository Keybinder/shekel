import re

f_mov_input = re.compile("[a-gA-G][1-8] [a-gA-G][1-8]")

blank_board = [[' ' for x in range(8)] for x in range(7)]

def set_board(in_board_f="boardstart.txt"):
     try:
          
          

def parse_move(move):
     # This function parses a move in the format that a user would provide;
     # it returns a tuple of four values as array references to the board if
     # the move is valid and returns None otherwise.
     move = move.strip()
     if re.match(f_mov_input, move):
         # Returns array
         print("move valid")
     else:
         # Returns None
         print("move invalid")
