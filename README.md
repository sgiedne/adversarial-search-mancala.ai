Mancala
=======

This is a Mancala game that allows a human to play against an intelligent computer. 
The computer chooses its moves using a minimax lookahead and alpha-beta pruning. 

Rules of Mancala:

* Object:  Two players compete against each other trying to get as many stones as possible before one of the players clears his or her side of all its stones.

+ Set Up:  The players sit facing each other with the board between them.  Each player is allocated the row of bins closest to him or her and a larger scoring bin, called a mancala, to the right.  Four stones are placed in each of the 12 smaller bins.  The players decide who goes first by flipping a coin.

+ Play:  The first player picks up all the stones in any of his or her six bins.  He/she then places, consecutively, one stone in each bin to the right (counterclockwise) around the board, including his/her own mancala, but not the opponent’s mancala.  If the player places the last stone in his/her own mancala, he/she is done with their turn.  If the last stone is placed in an empty bin on the player’s own side, he/she gets all the stones in the opponent’s bin directly across from his/her bin (if there are any stones). All captured stones plus the capturing stone go in the player’s mancala.  

+ Winning:  The game ends when one of the players runs out of stones in his/her small bins.  When this happens, the other player gets to place any stones remaining in his/her bins into his/her mancala.  The winner is the one with the most stones in his/her mancala.


Python files:
<p> 1. MancalaGame.py = creates Mancala board, defines game moves, defines game rules </p>
<p> 2. MancalaGUI.py = creates visual of game board </p>
<p> 3. Player.py = creates different player options </p>

Player options: 
<p> HUMAN = human as the player </p>
<p> RANDOM = random legal moves </p>
<p> MINIMAX = uses minimax algorithm to choose next move</p>
<p> ABPRUNE = uses alpha-beta pruning algorithm to choose next move</p>
<p> NYG316 = most optimal player using ab-pruning </p>

To play:
<p>#define players (can choose any above player options)</p>
<p>>>>player1=Player(1, Player.HUMAN)</p>
<p>>>>player2=Player(2, Player.HUMAN)</p>
<p>>>>startGame(player1, player2)</p>
<p>#if you do not have another human to play against, choose one of the computer player options</p>
