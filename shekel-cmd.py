# Shekel command-line v0.0.1

import shekel as s

constants = s.Constants()

startupmsg = """Shekel v0.0.1 alpha
Written by Jonah Hopkin, Licensed under <license> 2017
Type 'help' for help or 'newgame' to start a new game.
"""

command_dict = {
    'help':'help()',
    'newgame':'newgame()',
    'move':'',
    'options':'',

}

def display_board(bobject, x=1, y=0, gridref=True, compact=False): #add colours? orientation
     board, turn = bobject.board, bobject.turn
     gridnums = [i for i in range(8,0,-1)]
     gridletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

     for i in range(8):
          if gridref == True:
               line = str(gridnums[i]) + "|"
          elif gridref == False:
               line = ""
          for j in board[i]:
               line = line + (x * ' ') + constants.binp_dict[j]
          if gridref == False or y == 0:
               print(line + (y * '\n'))
          else:
               print(line + (y * '\n |'))
               # pretty sure this shouldn't work but it does

     if gridref == True:
          print((" +") + ('-' * (7 + 7 * x))) # these are display characters
          # don't freak out, this isn't eldritch maths
          lastline = "  "
          for i in gridletters:
               lastline = lastline + (x * ' ') + i
          print(lastline)

     if compact == False:
          print('')

def menu():
    print(startupmsg)
    user_in = input('> ').strip()
    tokens = user_in.split()


bobject = s.load_board()
display_board(bobject)
s.check_captures(bobject)

while True:
     user_in = input('> ')
     if s.parse_move(user_in) != None:
          move = s.parse_move(user_in)
          s1, s2, f1, f2 = move
          print(s.is_legal_move(bobject, move))
          bobject.move(move)
          display_board(bobject)
          print(s.check_captures(bobject))
     else:
          print("Try Again.")
