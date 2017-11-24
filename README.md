# shekel
Repository of files to run the Shekel board game.
This should contain all non-standard modules and files that the program uses for data.

Shekel is a 2-player board game played on a 7x8 board (7 columns, 8 rows), and has three different types of pieces: the shekel, 
the whekel and the fisher. In command-line versions, they are represented by the characters 's', 'w' and 'x' respectively ('x' 
is used instead of 'f' to prevent confusion with grid references). Each piece can be either white or black, represented as 
being uppercase or lowercase (e.g. 'S' denotes a white shekel, 'x' a black fisher). Each piece can move in their own fashion:
  - The shekel can move one space forward vertically on its turn
  - The whekel can move one space diagonally in any direction on its turn
  - The fisher can move one space in any direction (diagonal, vertical and horizontal) on its turn
The starting positions for the board are denoted in 'boardstart.txt' in command-line notation. White has the first turn.

The objective of the game is to get as many of your shekels to the far row of the board. Once a shekel reaches that row, it is 
removed from the game and a point is added to the player to whom the piece belongs.

Turn alternates between white and black; each turn consists of one move (and subsequent captures).

!TODO: Write rules for captures

There exists three planned levels of board representation in Shekel:
  1. Binary (3 digits), used internally for logic, pseudo-bitboard style.
  2. ASCII (up to 7 possible chars), used for command-line versions of the game and possibly save states.
  3. Graphical, used in user-level versions of the game (with pygame).
