#@author Luis Hinkhouse, Boogun Choi
#@date Feb. 23, 2017
#mailto: luishinkhouse@gmail.com
#mailto: boogun-choi@uiowa.edu
#
#@version 0.0
#TheChessPiece

#object property

#the name is what the chess piece is called: pawn, rook, bishop, knight, queen, king
name = ""
#16 letter code having 1's and 0's. 1 is able 0 is not. Each place represents a specific move.
move = ""
#the importance goes from 0-5. 0 meaning the most important, 5 meaning least. 0 is king, 1 is queen, 2 is knight, 3 is rook, 4 is bishop, 5 is pawn, -1 is no value
# possibly for v1 and v2, have the user be able to pick their importance levels
importance = -1
# True == black, False == white. user automatically starts as white. -1 means that it is not set up yet
black = -1
# represents horizontal axis of the x-y coordinate sysetm, can have 1~9 integer values
location_x = -1
# represents vertical axis of the x-y coordinate sysetm, can have 1~9 integer values
location_y = -1
# represents the piece can die by the next move, True == piece can die, False == piece is safe
danger = False
# represents the piece is not killed yet, True == not dead, False == dead
alive = True
# represents the piece's sole property, True == can move back, False == can't move back
moveback =  
