import Queue as Q
import random

#######################-----------------UTILITY FUNCTIONS--------------------------################

#####################################################################################################
#                   function to convert strings in file to a list of lists (Board)                  #
#####################################################################################################
def convertBoard(filename):
    board=()
    raw=()
    checks=0

    fileHandle= open(filename,'r')
    firstLine=fileHandle.readline().strip(';\n').split(',')
    board_size=int(firstLine[0])
    small_row=int(firstLine[1])
    small_col=int(firstLine[2])
    #print "\n boardsize,smallrow,smallcol=",board_size,small_row,small_col

    raw= fileHandle.readlines()
    if(len(raw)!=board_size):
        print "\n Wrong Input. Board size doesn't match"
        exit(0)

    board = [[0 for x in range(board_size)] for x in range(board_size)]

    for i in range(0,board_size):
        raw[i]=raw[i].strip(';\n')

    for i in range(0,board_size):
        x=raw[i].split(',')
        if(len(x)!=board_size):
            print "\n Wrong Input. Board size doesn't match"
            exit(0)
        for j in range(0,board_size):
            if not x[j]=='-':
               board[i][j]=int(x[j])
    #print "\n return from convert board"
    return board,board_size,small_row,small_col


#####################################################################################################
#                   board_validate function                                                         #
#####################################################################################################

def boardValidate(digit,board, board_size,row,col,small_row,small_col):

    value=digit
    for i in range (0,board_size):
        if board[i][col]==value:
            return False
        if board[row][i]==value:
            return False
    #check which small box does the value lie in
    box_row_start=row-(row%small_row)
    box_col_start=col-(col%small_col)

    for i in range(box_row_start,box_row_start+small_row):
         for j in range(box_col_start,box_col_start+small_col):
             if value==board[i][j]:
                 return False
    return True

#####################################################################################################
#                   Function to find Next Row and Column for Backtracking                           #
#####################################################################################################

def findNextPos(board, board_size):

    for i in range(0,board_size):
        for j in range(0,board_size):
            if board[i][j]==0:
                return i,j  #return the next position which is a hole
    return -1,-1    #if the whole board is complete means that sudoku completed
                    #return out of board value and check it in the basr condition for recursion

#####################################################################################################
#                   Function to find Next Row and Column for Backtracking+MRV                       #
#####################################################################################################
def findNextPosMRV(board, board_size,small_row,small_col):
    minPos=0
    i=0
    j=0

    board_dict=updateDict(board,board_size,small_row,small_col,board_dict={})
    minValue=999

    for elements in board_dict:

        if minValue>len(board_dict[elements]) :
            minValue=len(board_dict[elements])
            minPos=elements
    return minPos,board_dict[minPos]
#####################################################################################################
#                   Function to update valid moves                                                  #
#####################################################################################################

def updateDict(board, board_size,small_row,small_col,board_dict):
    pos=0
    #print "\n in update dict"
    for i in range(0,board_size):
        for j in range(0,board_size):
            if board[i][j]==0:
                pos=(board_size*i)+j  #this position is used as key for dictionary hashing
                list=findAllValidValues(board,board_size,small_row,small_col,i,j)
                board_dict[pos]=list
                #print board_dict
    return board_dict

#####################################################################################################
#                   Find all Valid values that the cell can take                                  #
#####################################################################################################

def findAllValidValues(board,board_size,small_row,small_col,row,col):

    valid_moves = [x for x in range(1,board_size+1)] #initialize list with all values

    for i in range(0,board_size):
        if board[i][col]!=0:
            if board[i][col] in valid_moves:
                valid_moves.remove(board[i][col])

        if board[row][i]!=0:
            if board[row][i] in valid_moves:
                valid_moves.remove(board[row][i])
    box_row_start=row-(row%small_row)
    box_col_start=col-(col%small_col)

    for i in range(box_row_start,box_row_start+small_row):
         for j in range(box_col_start,box_col_start+small_col):
             if board[i][j] in valid_moves:
                valid_moves.remove(board[i][j])
    return valid_moves

#####################################################################################################
#                  update the list using LCV property as key                                       #
#####################################################################################################

def updateList(board,board_size,unassigned_row,unassigned_col,small_row,small_col,board_dict_list):
    a=[]
    LCV_list=[]
    for value in board_dict_list:
        board[unassigned_row][unassigned_col]=value
        board_dict=updateDict(board,board_size,small_row,small_col,board_dict={})
        sum=0
        for element in board_dict:
            sum=sum+len(board_dict[element])
        a.append((sum,value))

    a=sorted(a,key=getKey,reverse=True)

    for i in range(0,len(a)):
        LCV_list.append(a[i][1])
    return LCV_list

def getKey(item):
    return item[0]

#####################################################################################################
#                  Find the next random move                                                      #
#####################################################################################################

def findNextPosRand(board,board_size,small_row,small_col,board_closed):
    conflictedDict={}
    for i in range(0,board_size):
        for j in range(0,board_size):
            #for every position check number of conflicts

            sum=0
            for k in range(0,board_size):
                if(board[i][j]==board[i][k] and k!=j):
                    sum=sum+1
                if(board[i][j]==board[k][j] and k!=i):
                    sum=sum+1

            box_row_start=i-(i%small_row)
            box_col_start=j-(j%small_col)

            for k in range(box_row_start,box_row_start+small_row):
                 for l in range(box_col_start,box_col_start+small_col):
                     if board[i][j]==board[k][l] and i!=k and j!=l :
                        sum=sum+1
            if sum>0 and (board_size*i+j) not in board_closed:
                conflictedDict[board_size*i+j]=sum
    while True:
        randPos=random.randrange(0,board_size*board_size)
        if randPos in conflictedDict and randPos not in board_closed:
            #print conflictedDict
            return randPos

#####################################################################################################
#                  Check Arc Consistency                                                           #
#####################################################################################################


def backwardConsistent(board_dict):
    for element_upper in board_dict:
        for element_lower in board_dict:
            if len(board_dict[element_lower])==1 and board_dict[element_upper]==board_dict[element_lower] and element_lower!=element_upper:
                return False
    return True


#####################################################################################################
#                   Function to find if board completed                                             #
#####################################################################################################

def boardFull(board,board_size):
    for i in range(0,board_size):
        for j in range(0,board_size):
            if board[i][j]==0:
                return False
    return True

#####################################################################################################
#                  To find if the solution has been reached                                          #
#####################################################################################################

def solutionReached(board,board_size,small_row,small_col):
    for i in range(0,board_size):
        for j in range(0,board_size):
            if not boardValidate(board[i][j],board,board_size,i,j,small_row,small_col):
                return False
    return True


#####################################################################################################
#                   Function to print the Final State                                               #
#####################################################################################################

def printBoard(board,board_size):
    for i in range(0,board_size):
        print(board[i])

#####################################################################################################