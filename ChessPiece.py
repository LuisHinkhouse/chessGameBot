#@author Luis Hinkhouse 
#@date Feb. 23, 2017
#mailto: luishinkhouse@gmail.com
#
#@version 0.0
#TheChessPiece

#object property

#the name is what the chess piece is called: pawn, rook, bishop, knight, queen, king
name = ""
#16 letter code having 1's and 0's. 1 is able 0 is not. Each place represents a specific move.
move = ""
#the importance goes from 0-5. 0 meaning the most important, 5 meaning least. 0 is king, 1 is queen, 2 is knight, 3 is rook, 4 is bishop, 5 is pawn, -1 is no value
#possibly for v1 and v2, have the user be able to pick their importance levels
importance = -1
# True == black, False == white. user automatically starts as white. -1 means that it is not set up yet
black = -1
#
location
