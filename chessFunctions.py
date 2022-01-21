notationToPosDict = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7
    }

EMPTY_BOARD = [
        ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
        ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
        ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
        ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
        ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
        ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
        ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
        ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
        ]

# builds new board from black perspective
# helps with writing logic (zero index lists)
# pragmatic, not elegant
def buildBoard():
    board = [x[:] for x in EMPTY_BOARD]
    board[0] = ['wr','wn','wb','wq','wk','wb','wn','wr']
    board[1] = ['wpa','wpb','wpc','wpd','wpe','wpf','wpg','wph']
    board[6] = ['bpa','bpb','bpc','bpd','bpe','bpf','bpg','bph']
    board[7] = ['br','bn','bb','bq','bk','bb','bn','br']
    return board

def findPiecePos(board, piece):
    for i, e in enumerate(board):
        try:
            return i, e.index(piece)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(piece)))
    
def convertNotationToPos(move):
    x = int(move[1]) - 1
    y = notationToPosDict.get(move[0])
    
    return x,y