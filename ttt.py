'''
test

Because this is a large project, we will complete the project in
parts. Each lesson leading to the final tic-tac-toe game will
make the game MORE complete. 

FIRST read a description of the game in the file INTRO.txt,
and make sure you understand the overall game and terminology we
will use. THEN, proceed with this file.

============ THE CODE ============

Our main data structure will be a 2D list:
BOARD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

This 2D 3x3 list-of-lists that represents the state of the game by
storing the 'markings' on each of the 9 positions.

The elements are strings (single characters) and represent either:
    (a.) An empty, unmarked position
        (Any number as a string from '1' to '9')
    (b.) A marking from player X (an 'X')
    (c.) A marking from player O (an 'O')

The main() function is the, well, main function of the game!
It runs a game loop that terminates when there is a winner or a tie.
For each loop, it alternates asking player X and player O to enter
an integer representing one of the unmarked positions in the board.
==================================


============ # TODO 0 ============
Explore the code at the code in the main() function,
until you can answer the following questions (based on the
code):
1. Under what condition does the game end? It ends when one of the player wins or if the game is tied.
2. What step(s) are "missing" from our
main() function to run the game correctly? It doesn't say that it will mark and X or an O wherever the player wishes to put their marker.
    (HINT: Who wins?, how do we mark the board?)
==================================

============ # TODO 1 ============
Complete (get_current_player) that returns 'X' when
it is player X's turn (when turn is even) and
returns 'O' when it is player 'O's turn.
==================================

============ # TODO 2 ============
Note that we can also 'flatten' the board
from 2D format to 1D format. The 2D format
will help in checking winners, and the 1D
format will help in formatted printing.

       2D                                    1D
[
    ['1', '2', '3'],     flattened
    ['4', '5', '6'],     ======>   ['1', '2', '3', '4', '5', '6', '7', '8', '9']    
    ['7', '8', '9'],
]

Complete the (flatten) function to turn any 2D board into a 1D board.
Once finished, read the print_board function to see how it uses flatten.
==================================


============ # TODO 3 ============
Complete the function (is_unmarked). Given a 2D 3x3 board (board_2d) and a
position from 1-9 (pos) return True if position (pos) of (board_2d) is
currently unmarked, else False.

HINT: What function you just wrote turns a 2D board into a 1D board?
HINT: What conditions do we need to check that a board position is unmarked?
    Check out the str.isdigit() method on the web.
    Or in IDLE:    
    >>> d = '4'
    >>> d.isdigit()
    True
    >>> 'X'.isdigit()
    False
    
HINT: Given a position (pos), the index at that position is (pos - 1)
(after appropriately converting str to int) as shown in the figure below:

(flattened empty board) ['1', '2', '3', '4', '5', '6', '7', '8', '9']

                (index)   0    1    2    3    4    5    6    7    8

==================================

Once you are finished with TODOs 0,1,2 and 3, use the following command
in freshly opened terminal to run the incomplete game:

cd python-problems/project
python3 -B ttt.py

What appears to be missing from the game so far?
'''

# In python, variables written here in all-capital
# are usually meant to represent useful constants/data
# we follow that convention except for BOARD, which
# is modified in the game loop

# some configuration information
NUM_PLAYERS = 2 # number of players
BOARD_DIM = 3 # size of board
NUM_POS = BOARD_DIM * BOARD_DIM  # number of board positions

# Template for formatting board markings into a
# printable tic-tac-toe board.
# triple quotes come in handy with multi-line strings!
# note that '\n' isn't written anywhere...
BOARD_TEMPLATE = '''
 {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
'''

# initial board values are all open positions (unmarked)
BOARD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

def get_current_player(turn):
    '''Given the game turn number, return 'X' if it is player X's turn.
    and 'O' if it is player O's turn.
    '''
    # TODO 1: YOUR CODE BELOW
    if turn % 2 == 0:
        return ("X")
    else:
        return ("O")

def flatten(board_2d):
    '''Given a 2D game board (board_2d),
    flatten it into a 1D representation as
    described in the problem statement.
    '''
    board_1d = []
    # TODO 2: YOUR CODE HERE
    for row in board_2d:
        for x in row:
            board_1d.append(x)
    return board_1d

def is_unmarked(board_2d, pos):
    '''Given a 2D 3x3 board (board_2d) and a position from 1-9 (pos)
    return True if the (pos) position of (board_2d) is unmarked. Else False.
    
    board_2d: List[List[str]]
    pos: int
    '''
    # convert board position (1-9) to index of the 1D board (0-8)
    # TODO 3: YOUR CODE HERE (replace None)
    board_1d = flatten(board_2d)
    idx = pos - 1
    board_value = board_1d[idx]
    if (board_value == "X") or (board_value == "O"):
        return False
    else:
        return True

def print_board(board_2d):
    '''Given a game board in 2D format, print it using the BOARD_TEMPLATE
    board_2d: a the game board in 2D format
    '''
    board_1d = flatten(board_2d)
    print(board_1d)
    # don't worry about the asterisk in *board_1d below: it takes
    # a list and 'unpacks' it by taking each list element and
    # inserting it as a separate argument to .format()
    print(BOARD_TEMPLATE.format(*board_1d))
    

# TODO 0:
def main():
    playing = True # the variable that keeps the game looping
    turn = 0 # which turn are we playing?
    while(playing):

        player = get_current_player(turn) # current player ('X' or 'O')

        print_board(BOARD)

        # prompt current player for position
        pos = int(input("Player {}, pick a position: ".format(player)))

        # mark the board at player's chosen position
        # (TODO NEXT WEEK)
        
        # update turn and winner
        turn += 1
        # playing ends when we have more turns than positions to mark
        playing = (turn < NUM_POS)
        

# Don't worry about this code.
# True if run directly by terminal/interpreter
if __name__ == '__main__':
    main()
