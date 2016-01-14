import pegSolitaireUtils
import config



def find_pegs(node_state):
    peg_list = []
    for i in range(0, 7):
        for j in range(0, 7):
            if (node_state[i][j] == 1):
                peg_list.append((i, j))
    return peg_list


def aStarOne(pegSolitaireObject):
    # the heuristic function can be defined as the number of pegs still pn board +
    # distance of (3,3) to the peg to be played
    start = pegSolitaireObject
    print start
    goal = [[-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1]]

    return True


def aStarTwo(pegSolitaireObject):
    #################################################
    # Must use functions:
    # getNextState(self,oldPos, direction)
    #
    # we are using this function to count,
    # number of nodes expanded, If you'll not
    # use this grading will automatically turned to 0
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you
    # reach goal using A-Star searching with second Heuristic
    # you used.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to return
    #
    #################################################
    return True
