import func
import random
###########################################
#   SUDOKU SOLVER- 5 FUNCTIONS/METHODS    #
###########################################


#   board consists of a list of list retrieved from the game.txt file
#   board_size is the max board length. Board Dimensions are board_size x board_size
#   small_row x small_col give the dimensions of the small grid
#   bool_value : captures the success/failure of completing the sudoku
#   board and checks return the final board state and number of consistency tests completed
#   both board and checks are declared as global variables
#   Each method has a main function which inturn calls the recursive function. This recursive function
#       is the actual function which computes the checks and solves the board. It retruns just the final
#       solution to its calling function



#####################################################################################################
#                                    BACKTRACKING                                                    #
#####################################################################################################

global board            # create global variables for board,checks and steps
global checks
global steps
steps=0
checks=0
def backtracking(filename):
    board,board_size,small_row,small_col=func.convertBoard(filename)  # convert the board
    bool_val,checks=backtrackingRecursive(board,board_size,small_row,small_col) # call the recursive function, get the final solution and #checks

    if (bool_val):      # if successfully completed execution then return board and checks with success mesage
       print("\n successfully completed sudoku. ")
    else:
        print("\n not completed board. ",bool_val)# if unsuccessful then return board and checks with failure mesage
        return(board,checks)

    return (board,checks)

#-----Backtracking Recursive Function----------#

def backtrackingRecursive(board,board_size,small_row,small_col):
    global checks
    unassigned_row,unassigned_col=func.findNextPos(board,board_size)
    if unassigned_col==-1 and unassigned_row==-1:
        return True,checks

    for digit in range (1,board_size+1):  # sequential execution
        checks=checks+1

        if(func.boardValidate(digit,board,board_size,unassigned_row,unassigned_col,small_row,small_col)==True):
            board[unassigned_row][unassigned_col]=digit  # digit assignemnt
            if( backtrackingRecursive(board,board_size,small_row,small_col)[0]==True): # recursive call
               return True,checks

            board[unassigned_row][unassigned_col]=0  # if backtracking then revert the last made move

    return False,checks

#####################################################################################################
#                                  BACKTRACKING + MRV                                               #
#####################################################################################################
def backtrackingMRV(filename):

    board=()
    global checks
    checks=0
    board,board_size,small_row,small_col=func.convertBoard(filename)

    bool_val,checks=backtrackingRecursiveMRV(board,board_size,small_row,small_col)# call the recursive function, get the final solution and #checks

    if (bool_val):   # if success
       print("\n successfully completed sudoku. ")
    else:
        print("\n not completed board. ",bool_val) # if failure
        return(board,checks)

    return (board,checks)

#-----Backtracking+MRV Recursive Function----------#

def backtrackingRecursiveMRV(board,board_size,small_row,small_col):
    global checks
    #base case
    if func.boardFull(board,board_size) :  # terminating state
        return True,checks

    minPos,board_dict_list=func.findNextPosMRV(board,board_size,small_row,small_col) # find the minimum remaining value pos and list of values
    unassigned_row=int(minPos/board_size) # convert to unassigned row and col value
    unassigned_col=minPos%board_size

    if (board_dict_list==[]):   # if list is empty
        return False,checks

    #board_dict_list=func.updateList(board,board_size,unassigned_row,unassigned_col,small_row,small_col,board_dict_list)

    for digit in board_dict_list:
            checks=checks+1
            board[unassigned_row][unassigned_col]=digit # value assignment
            if(backtrackingRecursiveMRV(board,board_size,small_row,small_col)[0]==True): # recursive call
                return True,checks
            board[unassigned_row][unassigned_col]=0  # revert the previous made move

    return False,checks

#####################################################################################################
#                                   BACKTRACKING + MRV + FORWARD PROPOGATION                        #
#####################################################################################################

def backtrackingMRVfwd(filename):
    board=()
    global checks
    checks=0
    board,board_size,small_row,small_col=func.convertBoard(filename)

    bool_val,checks=backtrackingRecursiveMRVfwd(board,board_size,small_row,small_col)# call the recursive function, get the final solution and #checks

    if (bool_val):   # sucess
       print("\n successfully completed sudoku. ")
    else:
        print("\n not completed board. ",bool_val) # failure
        return(board,checks)

    return (board,checks)

#-----Backtracking+MRV+fwd Recursive Function----------#

def backtrackingRecursiveMRVfwd(board,board_size,small_row,small_col):
    global checks
    #base case
    if func.boardFull(board,board_size) :
        return True,checks


    minPos,board_dict_list=func.findNextPosMRV(board,board_size,small_row,small_col) # find next pos and set of valid moves
    unassigned_row=int(minPos/board_size)
    unassigned_col=minPos%board_size

    #update the list with checks done to see if forward consistency is valid
    board_dict_list=func.updateList(board,board_size,unassigned_row,unassigned_col,small_row,small_col,board_dict_list)

    if (board_dict_list==[]):
                return False,checks


    for digit in board_dict_list:
            checks=checks+1
            board[unassigned_row][unassigned_col]=digit  # assignment of value

            if(backtrackingRecursiveMRVfwd(board,board_size,small_row,small_col)[0]==True): # recursive call
                return True,checks
            board[unassigned_row][unassigned_col]=0  # backtracking and reverting

    return False,checks

#####################################################################################################
#                                     BACKTRACKING + MRV + CONSTRAINT PROPOGATION                   #
#####################################################################################################

def backtrackingMRVcp(filename):
    board=()
    global checks
    checks=0
    board,board_size,small_row,small_col=func.convertBoard(filename)

    bool_val,checks=backtrackingRecursiveMRVcp(board,board_size,small_row,small_col)# call the recursive function, get the final solution and #checks

    if (bool_val):
       print("\n successfully completed sudoku. ") # success
    else:
        print("\n not completed board. ",bool_val) # failure
        return(board,checks)

    return (board,checks)

#-----Backtracking+MRV+CP Recursive Function----------#

def backtrackingRecursiveMRVcp(board,board_size,small_row,small_col):
    global checks
    #base case
    if func.boardFull(board,board_size) :
        return True,checks


    minPos,board_dict_list=func.findNextPosMRV(board,board_size,small_row,small_col) # find the next MRV pos and list of values
    unassigned_row=int(minPos/board_size)
    unassigned_col=minPos%board_size

    #update list for LCV sorted
    board_dict_list=func.updateList(board,board_size,unassigned_row,unassigned_col,small_row,small_col,board_dict_list)

    if (board_dict_list==[]):
        return False,checks
    #for every fwd consistent values
    for digit in board_dict_list:
        checks=checks+1
        board[unassigned_row][unassigned_col]=digit
        board_dict=func.updateDict(board,board_size,small_row,small_col,board_dict={})

        if(backtrackingRecursiveMRVcp(board,board_size,small_row,small_col)[0]==True): # recursive calls
            return True,checks

        board[unassigned_row][unassigned_col]=0  # backtracking and reverting last move made
    #check for backward consistency
    if func.backwardConsistent(board_dict)==False:
       return False,checks


    return False,checks

#####################################################################################################
#                                          MINIMUM CONFLICT                                         #
#####################################################################################################

def minConflict(filename):


    board=()
    checks=0
    board,board_size,small_row,small_col=func.convertBoard(filename)
    board_copy=board
    #func.printBoard(board_copy,board_size)
    board_closed=[]
    board_dict={}
    board_dict=func.updateDict(board,board_size,small_row,small_col,{})
    #find the board_closed cells
    for i in range(0,board_size):
        for j in range(0,board_size):
            if board[i][j]!=0:
                board_closed.append(board_size*i+j)

    #initialize board open cells with random values
    for i in range (0,board_size):
        for j in range (0,board_size):
            if board[i][j]==0:
                board[i][j]=random.randrange(1,board_size+1)


    bool_val,checks=minConflictRec(board,board_size,small_row,small_col,board_copy,board_dict,board_closed)# call the recursive function, get the final solution and #checks


    if (bool_val):
       print("\n successfully completed sudoku. ") # success
    else:
        print("\n not completed board. ",bool_val) # failure
        return(board,checks)

    return (board,checks)


#------------------MIN CONFLICT-------------------------------#

def minConflictRec(board,board_size,small_row,small_col,board_copy,board_dict,board_closed):
    global checks
    global steps


    if steps==300:  #limitng the number of steps to 300
        #func.printBoard(board,board_size)
        return False,checks
    #base case

    if func.solutionReached(board,board_size,small_row,small_col):
       #print("\n STEP  ......................",steps)
       #func.printBoard(board,board_size)
       return True,checks
    steps=steps+1
    randPos=func.findNextPosRand(board,board_size,small_row,small_col,board_closed) # find the next random pos from the set of conflicted positions
    unassigned_row=int(randPos/board_size) # calculate the unassigned col and row
    unassigned_col=randPos%board_size
    board_dict_list=board_dict[randPos]    # get the list of values from the dictionary for all the valid moves

    if(board_dict_list==[]):
        return False,checks

    if (randPos not in board_dict):
        return False,checks

    for digit in board_dict_list:
            checks=checks+1
            board[unassigned_row][unassigned_col]=digit # assignment

            if(minConflictRec(board,board_size,small_row,small_col,board_copy,board_dict,board_closed)[0]==True): # recursive calls
                #print "\n not backtracking"
                return True,checks
            board[unassigned_row][unassigned_col]=0 # backtracking and revert

    return False,checks