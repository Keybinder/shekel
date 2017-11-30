# Shekel command-line v0.0.1

import shekel as s

def display_board(board, x=1, y=0, gridref=True, compact=False): #add colours? orientation

     gridnums = [i for i in range(8,0,-1)]
     gridletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
     
     for i in range(8):
          if gridref == True:
               line = str(gridnums[i]) + "|"
          elif gridref == False:
               line = ""
          
          for j in board[i]:
               line = line + (x * ' ') + j
          if gridref == False or y == 0:
               print(line + (y * '\n'))
          else:
               print(line + (y * '\n |'))
               # pretty sure this shouldn't work but it does
          
     if gridref == True:
          print((" +") + ('-' * (7 + 7 * x)))
          lastline = "  "
          for i in gridletters:
               lastline = lastline + (x * ' ') + i
          print(lastline)

     if compact == False:
          print('')

shekel_board = s.set_board()
display_board(shekel_board)
