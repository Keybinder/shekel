import re
import copy

class Constants(): # put any reference values here
    def __init__(self):
        self.pbin_dict = {
             '.' : 0b000,
             'S' : 0b010,
             'W' : 0b100,
             'X' : 0b110,
             's' : 0b011,
             'w' : 0b101,
             'x' : 0b111
        }

        self.binp_dict = {v: k for k, v in self.pbin_dict.items()}
        # stolen from stackoverflow

#blank_board = [['.' for x in range(8)] for x in range(7)] #why is this needed?

class Board():
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
    def force_move(self, move):
        s1, s2, f1, f2 = move
        self.board[f1][f2] = self.board[s1][s2]
        self.board[s1][s2] = 0
    def move(self, move):
        s1, s2, f1, f2 = move
        if is_legal_move(self, move):
            self.board[f1][f2] = self.board[s1][s2]
            self.board[s1][s2] = 0
        else:
            print("That's an illegal move.")
        captures = check_captures(self, columns=[s2,f2])


# TODO: Make sure to keep Board objects standardised
# TODO: Make a scoring system

# ------------------------------------------------------------------------------

def load_board(in_board_f="boardstart.txt"): # Binary :)
     try:
         with open(in_board_f) as f:
             in_board = f.read()
     except FileNotFoundError:
         raise Exception("File not found when loading board.")
     except PermissionError:
         raise Exception("Permissions invalid; board not loaded.")
     # TODO: Add extra verification
     in_board = in_board.split('\n')
     main_board = []
     constants = Constants()
     turn = int(in_board[-1])
     del in_board[-1]
     for i in in_board:
         line_board = []
         for j in list(i):
             line_board.append(constants.pbin_dict[j])
         main_board.append(line_board)
     bobject = Board(main_board, turn)
     return bobject


# ------------------------------------------------------------------------------

def save_board(bobject, title):
    pass
    # TODO: Check if title already exists
    # Figure out how saving boards should even work

# ------------------------------------------------------------------------------

def check_captures(bobject, columns=[i for i in range(7)]):
    board, turn = bobject.board, bobject.turn
    captures = []
    for i in columns:
        vcol = [board[j][i] for j in range(8)]
        pblocks = []
        pblock = []
        psubblock = [0, 0, 0, 0] # colour, times repeated, first square with colour, last square with colour
        for x in range(8):
            piece = vcol[x]
            pcolour = piece % 2 # one of the advantages of the binary pieces
            is_blank = (piece >> 1 == 0b000)
            if is_blank and psubblock[1] != 0:
                psubblock[3] = x-1
                pblock.append(psubblock)
                pblocks.append(pblock)
                pblock = []
                psubblock = [0, 0, 0, 0]
            elif is_blank and psubblock[1] == 0:
                pass # because sequences of blank squares should not be counted
            elif not is_blank:
                if psubblock[0] == pcolour and psubblock[1] != 0:
                    psubblock[1] += 1
                elif psubblock[1] != 0: # previous square had diff colour
                    psubblock[3] = x-1
                    pblock.append(psubblock)
                    psubblock = [pcolour, 1, x, x]
                else: # previous square was blank
                    psubblock = [pcolour, 1, x, x]
                if x == 7: # check if final line
                    psubblock[3] = x
                    pblock.append(psubblock)
                    pblocks.append(pblock)

        # holy indentation, batman
        for block in pblocks:
            for j in range(len(block) - 1):
                # Standard shekel capture
                if block[j][1] > block[j+1][1]: # Standard capture 1
                    captures.append([block[j+1][2], i])
                if block[j][1] < block[j+1][1]: # Standard capture 2
                    captures.append([block[j][3], i])
                if len(block) >= 3 and j < len(block) - 2: # Saucy shekel
                    # NOTE: Future me, the line above might be the problem
                    if block[j+1][1] == 1:
                        captures.append([block[j+1][2], i])
                    # This is maybe fixed

    return captures

    # TODO: Make this function




# ------------------------------------------------------------------------------

def parse_move(usr_move): # Binary-valid :)

     # This function parses a move in the format that a user would provide;
     # it returns an array of four values as array references to the board if
     # the move is valid and returns None otherwise.

     # PLEASE NOTE THAT array references are given in the order such that the
     # row comes first and the column comes second i.e. opposite order that
     # the user would input. This should make assigning values to main board
     # straightforward.

     usr_move = usr_move.strip()

     if re.match(re.compile("[a-gA-G][1-8] [a-gA-G][1-8]"), usr_move):
         move_out = []
         usr_move = usr_move.split() # Gets the two references in an array
         for i in usr_move:
              for j in list(i):
                   move_out.append(j)
         # This f*cking sucks: reformatting to numbers
         for x in [0,2]:
              move_out[x] = int(ord(move_out[x].lower())) - int(ord('a'))
         for x in [1,3]:
              move_out[x] = 7 - (int(move_out[x]) - 1) # bit of a hack but works

         for x in [0,2]:
              move_out[x], move_out[x+1] = move_out[x+1], move_out[x] # swap

         return move_out

     else:
         return None

# ------------------------------------------------------------------------------

#def is_legal_move(move, board): # binary :)
def is_legal_move(bobject, move): # btuple is move, board, turn
     # TODO: Complete this function
     board, turn = bobject.board, bobject.turn
     s1, s2, f1, f2 = move
     legal_move = True
     start_square = board[s1][s2]
     fin_square = board[f1][f2]
     ptype = start_square >> 1
     pcolour = start_square % 2

     if start_square == 0b000:
          legal_move = False
     elif turn != pcolour:
          legal_move = False
     elif fin_square != 0b000:
          legal_move = False

     # Check if moving square is within range of piece VVV
     elif ptype == 0b001 and not (s2 == f2 and f1 == s1-1): # shekel
          legal_move = False
     elif ptype == 0b010 and not (abs(f1-s1) == abs(f2-s2) == 1): # whekel
          legal_move = False
     # The following is for the fisher
     elif ptype == 0b011 and not (2 > abs(f1-s1) >= 0 and 2 > abs(f2-s2) >= 0):
          # ^^^ i.e. not outside the range of 2 squares in any direction
          legal_move = False

     # TODO: Check if piece could be captured
     tempboard = Board(board, turn)
     tempboard.force_move(move)
     possible_captures = check_captures(tempboard, [f2])
     if [f1, f2] in possible_captures:
         legal_move = False
     reverse_move = f1, f2, s1, s2
     tempboard.force_move(reverse_move) # This is terrible but fixes issue
     return legal_move

# ------------------------------------------------------------------------------

def self_test():
    # TODO: Make this function
    pass
