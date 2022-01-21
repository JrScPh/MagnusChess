import chessFunctions as cf
import chessMoves as cm
import re

# chess game object
class Game:
    board = None
    turn = 0
    moves = []
    players = None
    # initialize board and set players
    def __init__(self, players):
        self.board = cf.buildBoard()
        self.players = players
        
    # prints board from white perspective
    # includes zero index coords
    def printBoardBlack(self):
        
        # print players, turn counter and upper letters
        print(self.players)
        print("Turn:",Game.turn)
        print("    7   6   5   4   3   2   1   0  ")
        print("    H   G   F   E   D   C   B   A  ")
        
        # print board, numbers, and lower letters
        for i in range(0,8):
            print(i,i + 1, end=' ')
            for j in range(7,-1, -1):
                if re.match("(bp|wp)[a-h]",self.board[i][j]):
                    print(self.board[i][j],end=' ')
                else:
                    print(self.board[i][j],end='  ')
            print(i + 1,i)
        print("    H   G   F   E   D   C   B   A  ")
        print("    7   6   5   4   3   2   1   0  \n")
        
        
    
    # prints board from black perspective
    # includes zero index coords
    def printBoardWhite(self):
        
        # print players, turn counter and upper letters
        print(self.players)
        print("Turn:", self.turn)
        
        print("    A   B   C   D   E   F   G   H  ")
        
        # print board, numbers, and lower letters
        for i in range(7,-1, -1):
            print(i,i + 1, end=' ')
            for j in range(0,8):
                if re.match("(bp|wp)[a-h]",self.board[i][j]):
                    print(self.board[i][j],end=' ')
                else:
                    print(self.board[i][j],end='  ')
            print(i + 1,i)
        print("    A   B   C   D   E   F   G   H  ")
        print("    0   1   2   3   4   5   6   7  \n")        
    
    # identifies piece and calls respective move function
    def movePiece(self, piece, move):
        if re.match("(bp|wp)[a-h]",piece):
            if cm.validatePawnMove(self.board, piece, move) == True:
                cm.updateBoard(self.board,piece,move)
                return True
            else:
                print("illegal move")
                return False
        else:
            print("Error: invalid piece\n")
        

