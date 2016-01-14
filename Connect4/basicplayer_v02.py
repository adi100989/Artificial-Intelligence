from util import memoize, run_search_function
myCount=0
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

###   Anshul: 9th oct: Changes Begin ###
def minimaxRecursive(board, depth,isMax, eval_fn = basic_evaluate,
            get_next_moves_fn = get_all_next_moves,
            is_terminal_fn = is_terminal, verbose = True):                  # THis method is initially called by another method minimax (written just below) and returns a tuple as (value, board with bestScore). Best Score for Min Node is minimum of its child and vie versa
    print "depth = ",depth

    if depth==0:    #base condition when depth is zero
        return eval_fn(board)    #return a tuple (Score/Value of terminal board, terminal board for that depth)

    MaxValue = (0,None)                 #Initial MaxValue or Maximum score is 0 and board is none
    MinValue = (float("inf"), None)     #Initial MinValue or Minimum score is infinity and board is none
    if isMax:                  #Meaning the Player is MAX
        value = -float("inf")
        for b in get_next_moves_fn(board):              #Iterating over all the possible boards b, that can be generated over board passed in function get_next_move_fn()
            value = minimaxRecursive(b[1], depth-1, not isMax, eval_fn, get_next_moves_fn, is_terminal_fn)          #Calling recursively with depth-1 and complementing isMax as MIN and MAX are at alternate level
            # MaxValue =e max(value, MaxValue)
            if MaxValue[0] < value[0]:                  #Note, both MaxValue and Value are tuples of the form (score/value, board). Now if value[0] is higher than our MaxValue, we will change the tuple MaxValue and update it with (new high score, corresponding board) since we are MAX and MAX chooses the highest value of it's child
                MaxValue = (value[0],b[1])              #we have changed the tuple MaxValue and update it with (new high score, corresponding board)
                #MaxValue[1]=b
          #for loop continues till all the childs b of board are remaining to be explored
        if verbose:
            print " player 1 selected Minvalue", MinValue,"   ",depth
        return MaxValue                                 #Returned the tuple MaxValue that has (Highest score, corresponding board with this highest score)
    else:                   # Meaning the player is MIN
        value = +float("inf")
        for b in get_next_moves_fn(board):
            value = minimaxRecursive(b[1], depth-1, not isMax,eval_fn, get_next_moves_fn, is_terminal_fn, True)
            if MinValue[0] >= value[0]:                 #Note, both MinValue and Value are tuples of the form (score/value, board). Now if value[0] is lower than our MinValue, we will change the tuple MinValue and update it with (new low score, corresponding board) since we are MIN and Min chooses the lowest value of it's child
                MinValue = (value[0],b[1])               #we have changed the tuple MinValue and update it with (new low score, corresponding board)
                #MinValue[1]=b
                #for loop continues till all the childs b of board are remaining to be explored
        if verbose:
            print " player 1 selected Minvalue", MinValue,"   ",depth

        return MinValue                                  #Returned the tuple MinValue that has (Lowest score, corresponding board with this lowest score)

def minimax(board, depth, eval_fn = basic_evaluate,
            get_next_moves_fn = get_all_next_moves,
            is_terminal_fn = is_terminal, verbose = True):              #This method compares the board at root and the 'boardNew' that we got to find out which column should max place the coin in.

   pair = minimaxRecursive(board,depth,True)                           #Note: pair is a tuple containing (Value/Score of best board, that boardNew with best score)
   boardNew = pair[1]
   print boardNew
   for i in range (0,6):                                                # (0 to 6) since we have only 6 rows
       for j in range (0,7):                                            # (0 to 6) since we have exactly 7 columns
           if board.get_cell(i,j) != boardNew.get_cell(i,j):
               return j                                                 #returns the column that is different in these two board. THis column is the one MAX should place it's coin on.

###   Anshul: 9th oct: Changes Ends ###

def rand_select(board):
    """
    Pick a column by random
    """
    import random
    moves = [move for move, new_board in get_all_next_moves(board)]
    return moves[random.randint(0, len(moves) - 1)]


def new_evaluate(board):
    #start evaluate function#



    raise NotImplementedError


random_player = lambda board: rand_select(board)
basic_player = lambda board: minimax(board, depth=4, eval_fn=basic_evaluate)        #Can make it 2 to understand better at shallow depth
#new_player = lambda board: minimax(board, depth=4, eval_fn=new_evaluate)
progressive_deepening_player = lambda board: run_search_function(board, search_fn=minimax, eval_fn=basic_evaluate)
