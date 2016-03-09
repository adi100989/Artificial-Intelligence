from util import memoize, run_search_function
import random
from copy import deepcopy


def basic_evaluate(board):
     #return random.randint(0,1000)
     if board.is_game_over():
         score = -1000
     else:
         score = board.longest_chain(board.get_current_player_id()) * 10
         # Prefer having your pieces in the center of the board.
         for row in range(6):
             for col in range(7):
                 if board.get_cell(row, col) == board.get_current_player_id():
                     score -= abs(3-col)
                 elif board.get_cell(row, col) == board.get_other_player_id():
                     score += abs(3-col)
         #score=random.randint(0,1000)
     return score


def get_all_next_moves(board):
    """ Return a generator of all moves that the current player could take from this position """
    from connectfour import InvalidMoveException

    for i in xrange(board.board_width):
        try:
            yield (i, board.do_move(i))
        except InvalidMoveException:
            pass

def is_terminal(depth, board):
    """
    Generic terminal state check, true when maximum depth is reached or
    the game has ended.
    """
    return depth <= 0 or board.is_game_over()


########    https://en.wikipedia.org/wiki/Negamax     #########
def minimax_nega_value (board, depth):

    global col
    global expandedNodes

    if is_terminal(depth,board):
       return (basic_evaluate(board))
    max_value=-1*float("inf")
    #max_tuple = (-1*float("inf"),board ,0)
    expandedNodes = 1
    return_value=0
    col = 0
    for moves in get_all_next_moves(board):
        return_value=-1*minimax_nega_value(moves[1],depth-1)  # this is a tuple which returns (score,board,expanded nodes)
        expandedNodes = expandedNodes + return_value_tuple[2]    #increment the expanded nodes
        #return_value = return_value_tuple[0]*-1                  #invert the value tuple value

        if max_tuple[0]<return_value:
            #max_value = return_value_tuple
            max_tuple=(return_value,return_value_tuple[1],return_value_tuple[2])
            col=moves[0]

        print "max value= ",max_tuple[0]
        print "return value at 0= ",return_value_tuple[0]
        print "return value = ",return_value
        print "col =",col
        print "nodes expanded =",max_tuple[2]
    #tuple = (max_value,col,expandedNodes)
    #print("tuple returned= %f ,%d , %d" %(tuple[0],tuple[1],tuple[2]))
    return max_tuple


def minimax(board, depth, eval_fn = basic_evaluate,
            get_next_moves_fn = get_all_next_moves,
            is_terminal_fn = is_terminal,
            verbose = True):
    #max_value=float("inf")
    #expandedNodes = 0
    max_value_tuple=minimax_nega_value(board,depth-1)
    print "total expanded nodes ", max_value_tuple[2]
    return col
    '''for moves in get_all_next_moves(board):
        evaluated_value_tuple= minimax_nega_value(moves[1], depth-1)
        expandedNodes = expandedNodes + evaluated_value_tuple[2]
        evaluated_value= evaluated_value_tuple[0]*-1
        #max_value=max(max_value, evaluated_value)
        #move_made=moves[0]
        if max_value<evaluated_value:
            #max_value = return_value_tuple
            max_value=evaluated_value
            move_made=moves[0]
            max_value_tuple=tuple(max_value,moves[0],moves[1],expandedNodes)

    print "total expanded nodes ", expandedNodes
    return max_value_tuple[1]
    '''

def rand_select(board):
    """
    Pick a column by random
    """
    import random
    moves = [move for move, new_board in get_all_next_moves(board)]
    return moves[random.randint(0, len(moves) - 1)]


def new_evaluate(board):
    raise NotImplementedError


random_player = lambda board: rand_select(board)
basic_player = lambda board: minimax(board, depth=3, eval_fn=basic_evaluate)
#new_player = lambda board: minimax(board, depth=4, eval_fn=new_evaluate)
progressive_deepening_player = lambda board: run_search_function(board, search_fn=minimax, eval_fn=basic_evaluate)
