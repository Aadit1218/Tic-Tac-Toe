'''
Because this is a large project, we will complete the project in
parts. Each lesson leading to the final tic-tac-toe game will
make the game MORE complete. 

FIRST read a description of the game in the file INTRO.txt,
and make sure you understand the overall game and terminology we
will use. THEN, proceed with this file.

============ THE CODE ============

Our main data structure will be a 2D list:
board = [
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


============ # TODO 4 ============
Recall that last time we flattened a 2D list into
a 1D list. Note that we can also 'unflatten' a 1D board
from 1D format to 2D format:

                   1D                                            2D                            
                                                            [
                                              unflatten      ['1', '2', 'X'],
['1', '2', 'X', '4', '5', '6', 'O', '8', '9'] ==========>    ['4', '5', '6'],
                                                             ['O', '8', '9'],
                                                            ]

Complete the (unflatten) function to turn any 1D board into a 2D board.
You may assume the 2D board is always 3x3 (BOARD_DIM * BOARD_DIM).

HINT: Recall that we can get a range of list elements with splicing:
        suppose s = [1,2,3,4,5,6,7,8,9]
        then s[i:j] gets the range from index i (inclusive, start index)
        to index j (exclusive, stop index)

        >>> s[0:3]
        [1,2,3]
        
        >>> s[3:6]
        [4,5,6]
        
        >>> s[6:9]
        [7,8,9]

        Note that s[0:3], s[3:6], s[6:9] would be the 'rows' of the
        2D format. What can you do with this?
==================================


============ # TODO 5a ============
Complete the function (mark), which is given the state of the board
in 2D format (board_2d), the board position (pos), and the current player
('X' or 'O') as (player), and returns the state of the board in 2D format
after the player marks the position on the board.

HINT: You may use/call other functions in this file you have written when
writing the code for (mark). Just know that calling the SAME function in it's
own definition is called recursion (we'll talk about this later, just know
to avoid it for this project e.g. don't call my_func() in the definition of
my_func)

HINT: How do we flatten board_2d into a 1D board?

HINT: Once we have a 1D board, how can use indexing to set the
        correct element to the player's mark (player)?
        
HINT: Once we have a 1D board how do we set the correct element
        to the player's mark?
        
HINT: Once we set the player's mark in the 1D board, how do we convert
        this marked 1D board into an equivalent 2D board (which is
        what we return)?
==================================


============ # TODO 5b ============
In the while-loop of the function (main),
we first:
    1. get the current player
    2. print the current state of the board
    3. ask the player for a position to mark
    
after getting the integer position from user input (pos),
we need to mark the board at the position with the player's mark.

TODO 5a asked you to write the (mark) function. Now for TODO 5b,
you must call the (mark) function in (main) and set the
(board) variable to mark's return value.
==================================

============ # TODO 6 ============
Once you are finished with the TODO 4, TODO 5a, and TODO 5b, run the incomplete
game using the following command in a freshly opened terminal. Then, answer the
questions (as you typed last time).

cd python-problems/project
python3 -B ttt.py

Now that we've made new changes, what appears to be missing from
the game so far?





Can you (briefly) describe an algorithm (in english/pseudocode)
to finish the game?


==================================
'''

# In python, variables written here in all-capital
# are usually meant to represent useful constants/data

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

def get_current_player(turn):
    '''Given the game turn number, return 'X' if it is player X's turn.
    and 'O' if it is player O's turn.
    '''
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
    for row in board_2d:
        for x in row:
            board_1d.append(x)
    return board_1d

def unflatten(board_1d):
    '''Given a 1D game board (board_1d),
    unflatten it into a 2D representation as
    described in the problem statement.
    '''
    # TODO 4: YOUR CODE BELOW (replace None below)
    
    board_2d = [board_1d[0:3], board_1d[3:6], board_1d[6:9]]
    return board_2d


def is_unmarked(board_2d, pos):
    '''Given a 2D 3x3 board (board_2d) and a position from 1-9 (pos)
    return True if the (pos) position of (board_2d) is unmarked. Else False.
    
    board_2d: List[List[str]]
    pos: int
    '''
    board_1d = flatten(board_2d)
    # convert board position (1-9) to index of the 1D board (0-8)
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
    # don't worry about the asterisk in *board_1d below: it takes
    # a list and 'unpacks' it by taking each list element and
    # inserting it as a separate argument to .format()
    print(BOARD_TEMPLATE.format(*board_1d))

def mark(board_2d, pos, player):
    '''Given a game board in 2D format (board_2d),
    an integer position from 1 to 9 (pos),
    and the player's mark as a string, 'X' or 'O' (player),
    
    return a new board (new_board_2d) in 2D format so that the returned
    board is the same as board_2d, except that it contains the player's
    mark (player) at the position (pos). Remember that pos is not an index,
    but the numbered position 1-9.
    
    
    board_2d: List[List[str]]
    pos: int
    player: str ('X' or 'O')
    '''
    # TODO 5a: YOUR CODE BELOW


    board_1d = flatten(board_2d)
    idx = pos - 1
    board_1d[idx] = player
    new_board_2d = unflatten(board_1d)
    return new_board_2d

def find_winner(board_2d):
    '''
    board_2d: board in 2D format with numbers or X or O (List[List[str]])

    [
        ['1', '2', 'X'],
        ['4', '5', '6'],
        ['O', '8', '9'],
    ]

    return value: 'X' (player X wins), 'O' (player O wins), '' (tie, or game in progress)
    '''
    
    # check the 3 vertical wins
    for col_idx in range(BOARD_DIM): # 0, 1, 2
        #check each column
        # are all the positions in col_idx the same?
        all_same = ((board_2d[0][col_idx] == board_2d[1][col_idx]) and (board_2d[1][col_idx] == board_2d[2][col_idx]))
        winner = board_2d[0][col_idx]
        if (all_same):
            return winner
    # done with vertical check

    # check the 3 horizontal wins
    # TODO: 7

    for row_idx in range(BOARD_DIM):
        horizontal = ((board_2d[row_idx][0] == board_2d[row_idx][1]) and (board_2d[row_idx][1] == board_2d[row_idx][2]))
        winner = board_2d[row_idx][0]
        if (horizontal):
            return winner
    # check the 2 diagonal wins
    # TODO: 8
    diagonal = ((board_2d[0][0] == board_2d[1][1]) and (board_2d[1][1] == board_2d[2][2]))
    diagonal_1 = ((board_2d[0][2] == board_2d[1][1]) and (board_2d[1][1] == board_2d[2][0]))
    winner = board_2d[1][1]
    if(diagonal or diagonal_1):
        return winner

    # if still here after all checks,
    return ''

def main():
    # initial board values are all open positions (unmarked)
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]
    
    playing = True # the variable that keeps the game looping
    turn = 0 # which turn are we playing?
    while(playing):

        player = get_current_player(turn) # current player ('X' or 'O')

        print_board(board)

        # prompt current player for position
        pos = int(input("Player {}, pick a position: ".format(player)))

        # TODO 5b: mark the board at player's chosen position
        # YOUR CODE HERE
        board = mark(board, pos, player)
        #return board
    
        # TODO NEXT WEEK: determine a winner
        winner = find_winner(board)# 'X', 'O', ''
        breakpoint()
        if turn == 8 and winner == '':
            print("It's a tie")
            
        # update turn
        turn += 1
        # playing ends when we have more turns than positions to mark
        playing = (turn < NUM_POS)

        if (winner == 'X' or winner == 'O'):
            playing = False
            print("player {} won!".format(winner))
        
    print_board(board)
    print("END OF GAME")
    
# Don't worry about this code.
# True if run directly by terminal/interpreter
if __name__ == '__main__':
    main()
