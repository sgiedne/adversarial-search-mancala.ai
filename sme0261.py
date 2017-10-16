# File: sme0261.py
# Author(s) names AND netid's:
# Santhosh Subramanian SSL4520
#Siddharth Muthukumaran SME0261
# Date: 10/15/2017
# Group work statement: All group members were present and contributing
# during all work on this project.
# Defines a simple artificially intelligent player agent
# You will define the alpha-beta pruning search algorithm
# You will also define the score function in the MancalaPlayer class,
# a subclass of the Player class.

from random import *
from decimal import *
from copy import *
from MancalaBoard import *
import sys
import time

# a constant
INFINITY = 1.0e400

class Player:
    """ A basic AI (or human) player """
    HUMAN = 0
    RANDOM = 1
    MINIMAX = 2
    ABPRUNE = 3
    CUSTOM = 4

    def __init__(self, playerNum, playerType, ply=7):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        self.ply = ply

    def __repr__(self):
        """Returns a string representation of the Player."""
        return str(self.num)

    def minimaxMove(self, board, ply):
        """ Choose the best minimax move.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue(nb, ply-1, turn)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue(nextBoard, ply-1, turn)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
        return score

    def minValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue(nextBoard, ply-1, turn)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
        return score


    # The default player defines a very simple score function
    # You will write the score function in the MancalaPlayer below
    # to improve on this function.
    def score(self, board):
        """ Returns the score for this player given the state of the board """
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return 0.0
        else:
            return 50.0

    # You should not modify anything before this point.
    # The code you will add to this file appears below this line.

    # You will write this function (and any helpers you need)
    # You should write the function here in its simplest form:
    #   1. Use ply to determine when to stop (when ply == 0)
    #   2. Search the moves in the order they are returned from the board's
    #       legalMoves function.
    # However, for your custom player, you may copy this function
    # and modify it so that it uses a different termination condition
    # and/or a different move search order.
    def alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        alpha = -INFINITY
        beta = INFINITY
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue_AB(nb, ply-1, turn, alpha, beta)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue_AB(self, board, ply, turn, alpha, beta):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue_AB(nextBoard, ply-1, turn, alpha, beta)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
            if beta <= score:
                return score
            if alpha < score:
                alpha = score
        return score


    def minValue_AB(self, board, ply, turn, alpha, beta):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue_AB(nextBoard, ply-1, turn, alpha, beta)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
            if alpha >= score:
                return score
            if score < beta:
                beta = score
        return score

#Custom alpha beta with improved score function
    def improved_alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        alpha = -INFINITY
        beta = INFINITY
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                player = sme0261(self)
                return (player.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.improved_minValue_AB(nb, ply-1, turn, alpha, beta)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def improved_maxValue_AB(self, board, ply, turn, alpha, beta):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            player = sme0261(turn)
            return player.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                player = sme0261(turn)
                return player.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.improved_minValue_AB(nextBoard, ply-1, turn, alpha, beta)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
            if beta <= score:
                return score
            if alpha < score:
                alpha = score
        return score


    def improved_minValue_AB(self, board, ply, turn, alpha, beta):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            player = sme0261(turn)
            return player.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                player = sme0261(turn)
                return player.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.improved_maxValue_AB(nextBoard, ply-1, turn, alpha, beta)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
            if alpha >= score:
                return score
            if score < beta:
                beta = score
        return score




    def chooseMove(self, board):
        """ Returns the next move that this player wants to make """
        if self.type == self.HUMAN:
            move = input("Please enter your move:")
            while not board.legalMove(self, move):
                print move, "is not valid"
                move = input( "Please enter your move" )
            return move
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            print "chose move", move
            return move
        elif self.type == self.MINIMAX:
            val, move = self.minimaxMove(board, self.ply)
            print "chose move", move, " with value", val
            return move
        elif self.type == self.ABPRUNE:
            val, move = self.alphaBetaMove(board, self.ply)
            print "chose move", move, " with value", val
            return move
        elif self.type == self.CUSTOM:
            # TODO: Implement a custom player
            # You should fill this in with a call to your best move choosing
            # function.  You may use whatever search algorithm and scoring
            # algorithm you like.  Remember that your player must make
            # each move in about 10 seconds or less.
            val, move = self.improved_alphaBetaMove(board, self.ply)
            print "chose move", move, " with value", val
            return move
        else:
            print "Unknown player type"
            return -1


# Note, you should change the name of this player to be your netid
class sme0261(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """
    def __init__(self, Player):
        self.num = Player.num

    def score(self, board):
        """ Evaluate the Mancala board for this player """
        # Currently this function just calls Player's score
        # function.  You should replace the line below with your own code
        # for evaluating the board

        #Base score begins at 100.
        base_score = 100

        #Add the current player's mancala's score to the base score
        base_score += board.scoreCups[self.num - 1]

        #Go through all the cups for the current player. If a cup is empty,
        #add one plus the number of pebbles in the directly opposite cup to
        #the base score. If the opponent's cup is empty, subtract the number of
        #pebbles in the corresponding current player's cup from the base score.
        #This heuristic indicates a potential chance of gaining/losing pebbles
        #from/to the opponent's side
        if self.num == 1:
            for i in range(len(board.P1Cups)):
                if board.P1Cups[i] == 0:
                    base_score += board.P2Cups[5-i] + 1
                if board.P2Cups[i] == 0:
                    base_score -= board.P1Cups[5-i]
        elif self.num == 2:
            for i in range(len(board.P2Cups)):
                if board.P2Cups[i] == 0:
                    base_score += board.P1Cups[5-i] + 1
                if board.P1Cups[i] == 0:
                    base_score -= board.P2Cups[5-i]


        #For this heuristic, the value of 6-i gives the ideal number of pebbles
        #that can be present in the cup. 6-i pebbles will ensure you don't drop
        #any pebbles onto the oppponent's side and will also add one pebble to
        #the current player's mancala. Go through all the cups for the current
        #player. For each cup, if there are exactly 6-i pebbles, add one to the
        #base score (the one pebble that goes into the current player's mancala
        #if this cup is played). If there are more than 6-1 pebbles, subtract
        #the number of pebbles that go to the oppoenent's side and add one for
        #the pebble that goes into the mancala. Do nothing when the cup has less
        #than 6-i pebbles
        if self.num == 1:
            for i in range(len(board.P1Cups)):
                if board.P1Cups[i] == (6-i):
                    base_score+=1
                elif board.P1Cups[i] > (6-i):
                    base_score -= (board.P1Cups[i] - (6-i) + 1)
        elif self.num == 2:
            for i in range(len(board.P2Cups)):
                if board.P2Cups[i] == (6-i):
                    base_score+=1
                elif board.P2Cups[i] > (6-i):
                    base_score -= (board.P2Cups[i] - (6-i) + 1)

        #In this heurstic we calcualte how far the current player's cups and
        #his mancala together are from 24 (half of total number of pebbles).
        #The difference is subtracted from the base score, only if the pebbles
        #on the current player's side is less than 24. The score remains
        #unaffected otherwise.
        if self.num == 1:
            if (sum(board.P1Cups) + board.scoreCups[self.num - 1]) <= 24:
                base_score -= (24 - sum(board.P1Cups) - board.scoreCups[self.num - 1])
        elif self.num == 2:
            if (sum(board.P2Cups) + board.scoreCups[self.num - 1]) <= 24:
                base_score -= (24 - sum(board.P2Cups) - board.scoreCups[self.num - 1])

        # return Player.score(self, board)
        return base_score
