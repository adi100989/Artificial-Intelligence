from util import memoize, run_search_function

def basic_evaluate(board):
    """
    The original focused-evaluate function from the lab.
    The original is kept because the lab expects the code in the lab to be modified.
    """
    if board.is_game_over():
        # If the game has been won, we know that it must have been
        # won or ended by the previous move.
        # The previous move was made by our opponent.
        # Therefore, we can't have won, so return -1000.
        # (note that this causes a tie to be treated like a loss)
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
def minimax_nega_value (board, depth, color):
    if is_terminal(depth,board):
        #print "is_terminal reached"
        return (color*basic_evaluate(board), board)

    max_value = float("inf")

    for moves in get_all_next_moves(board):
        return_value=-1*minimax_nega_value(moves[1],depth-1, -1*color)
        max_value=max(max_value, return_value)

        return max_value


def minimax(board, depth, eval_fn = basic_evaluate,get_next_moves_fn = get_all_next_moves,is_terminal_fn = is_terminal,verbose = True):
    max_value=float("inf")
    for moves in get_all_next_moves(board):
        evaluated_value= minimax_nega_value(moves[1], depth-1,1)
        max_value=max(max_value, evaluated_value)
        move_made=moves[0]
    return move_made


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
basic_player = lambda board: minimax(board, depth=4, eval_fn=basic_evaluate)
#new_player = lambda board: minimax(board, depth=4, eval_fn=new_evaluate)
progressive_deepening_player = lambda board: run_search_function(board, search_fn=minimax, eval_fn=basic_evaluate)
