import readGame
import config


#######################################################
# These are some Helper functions which you have to use 
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_wall(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################
class game:
    def __init__(self, filePath):
        self.gameState = readGame.readGameState(filePath)
        self.nodesExpanded = 0
        self.trace = []

    def is_corner(self, pos):
        ########################################
        # You have to make changes from here
        # check for if the new position is a corner or not
        # return true if the position is a corner
        #	print "is corner is called"
        if (pos == (0, 2) or pos == (0, 3) or pos == (0, 4) or pos == (1, 2) or
                    pos == (1, 4) or pos == (2, 0) or pos == (2, 1) or pos == (2, 5) or
                    pos == (2, 6) or pos == (3, 0) or pos == (3, 6) or pos == (4, 0) or
                    pos == (4, 1) or pos == (4, 5) or pos == (4, 6) or pos == (5, 4) or
                    pos == (5, 2) or pos == (6, 2) or pos == (6, 3) or pos == (6, 4)):
            return True
        # if(self.pos[0] == 0 or  self.pos[y] ==6 or self.pos[1]==1 or
        #   self.pos[2]==0 or  self.pos[y-1][] =='_' or self.pos[y+1][] =='_' or
        #   self.pos[x-1][] =='_' or self.pos[x+1][] =='_' )
        else:
            return False

    def getNextPosition(self, oldPos, direction):
        #########################################
        # YOU HAVE TO MAKE CHANGES HERE
        # See DIRECTION dictionary in config.py and add
        # this to oldPos to get new position of the peg if moved
        # in given direction , you can remove next line
        # oldPostemp = oldPos[0]+2*direction[0],oldPos[1]+2*direction[1]
        # oldPostuple = oldPos[0]
        # oldPos = oldPostuple[0]+2*config.DIRECTION[direction][0],oldPostuple[1]+2*config.DIRECTION[direction][1]
        oldPos = oldPos[0] + 2 * config.DIRECTION[direction][0], oldPos[1] + 2 * config.DIRECTION[direction][1]
        # print oldPos
        return oldPos

    def is_validMove(self, oldPos, direction):
        #########################################
        # DONT change Things in here
        # In this we have got the next peg position and
        # below lines check for if the new move is a corner
        newPos = self.getNextPosition(oldPos, direction)
        # midPos=oldPos[1]+direction[1],oldPos[1]+direction[1]
        midPos = oldPos[0] + config.DIRECTION[direction][0], oldPos[1] + config.DIRECTION[direction][1]
        # print midPos
        # genNew=newPos[1]+(7*newPos[0])
        # genMid=oldPos[1]+direction[1]+(7*(oldPos[1]+direction[1]))
        if self.is_corner(oldPos):
            return False
        #########################################

        ########################################
        # YOU HAVE TO MAKE CHANGES BELOW THIS
        # check for cases like:
        # if new move is already occupied
        # or new move is outside peg Board
        # Remove next line according to your convenience
        # Anshul, Checking if 1) Not out of Board 2) Not already Occupied 3) Position is available, ie: = 0 4) midPos = 1
        elif newPos[0] < 0 or newPos[0] > 6 or newPos[1] < 0 or newPos[1] > 6:  # Checked if outside the board
            return False
        elif self.gameState[newPos[0]][newPos[1]] == 1 or self.gameState[newPos[0]][
            newPos[1]] != 0:  # Checked if newPos is already occupied (==1), and if it is 0 and not -1
            return False
        elif self.gameState[midPos[0]][
            midPos[1]] != 1:  # Checked if midPos is 1 and nothing else, if it is something other than 1, return False
            return False
        # elif((self.gameState[newPos[0]][newPos[1]]== 0) and (self.gameState[midPos[0]][midPos[1]]== 1)):
        # #if(pegHolder[newPos[0]][newPos[1]]== 0):
        # 	return True
        else:
            return True  # Return true as a validMove since we checked for all wrong conditions.

    def getNextState(self, oldPos, direction):
        ###############################################
        # DONT Change Things in here
        self.nodesExpanded += 1
        if not self.is_validMove(oldPos, direction):
            print "Error, You are not checking for valid move"
            return False
        # exit(0)
        ###############################################

        ###############################################
        # YOU HAVE TO MAKE CHANGES BELOW THIS
        # Update the gameState after moving peg
        # eg: remove crossed over pegs by replacing it's
        # position in gameState by 0
        # and updating new peg position as 1
        else:
            newPos = self.getNextPosition(oldPos,
                                          direction)  # capture newPos from the return function of getNextPosition
            middlePeg = oldPos[0] + direction[0], oldPos[1] + direction[1]
            # pegHolder[newPos[0]][newPos[1]]=1                #convert
            # pegHolder[oldPos[0]][oldPos[1]]=0
            self.gameState[newPos[0]][newPos[1]] = 1
            self.gameState[middlePeg[0]][middlePeg[1]] = 0
            self.gameState[oldPos[0]][oldPos[1]] = 0
            return self.gameState
