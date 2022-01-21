import chessFunctions as cf
import re

def validatePawnMove(board,piece,move):
    
    # en passant is not yet implemented
    
    # get coordinates
    a,b = cf.findPiecePos(board,piece)
    x,y = cf.convertNotationToPos(move)
            
    # validate white pawn move
    
    # forward two on first move
    if re.match("w(.|..)",piece):
        if a == 1 and x == 3 and b == y:
            if re.match("b(.|..)",board[x][y]):
                    return False
            return True 
        # forward one
        elif x == (a + 1) and b == y:
            if re.match("b(.|..)",board[x][y]):
                    return False
            if x == 7 and b == y:
                print("promote",piece,"to queen")
            return True
        # capture black piece
        elif x == (a + 1) and y == b + 1:
            if re.match("b(.|..)",board[a+1][b+1]):
                return True
        elif x == (a + 1) and y == b - 1:
            if re.match("b(.|..)",board[a+1][b-1]):
                return True
        else:
            return False
    else:
        
        # validate black pawn move
        
        # forward two on first move    
        if a == 6 and x == 4 and b == y:
            if re.match("w(.|..)",board[x][y]):
                    return False
            return True 
        # forward one
        elif x == (a - 1) and b == y:
            if re.match("w(.|..)",board[x][y]):
                    return False
            if x == 0 and b == y:
                print("promote",piece,"to queen")
            return True
        # capture black piece
        elif x == (a - 1) and y == b - 1:
            if re.match("w(.|..)",board[a-1][b-1]):
                return True
        elif x == (a - 1) and y == b + 1:
            if re.match("w(.|..)",board[a-1][b+1]):
                return True
        else:
            return False

def updateBoard(board,piece,move):
    a,b = cf.findPiecePos(board,piece)
    x,y = cf.convertNotationToPos(move)
    board[a][b] = cf.EMPTY_BOARD[x][y]
    board[x][y] = piece