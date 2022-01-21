import unittest
import chessGame as cg
import chessFunctions as cf
import chessMoves as cm
import sys,os

# these functions help to clean up console output
# while debug print statements are still in the code

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class TestBuildBoard(unittest.TestCase):
    
    def test_verify_board(self):
        testBoard = [
            ['wr','wn','wb','wq','wk','wb','wn','wr'],
            ['wpa','wpb','wpc','wpd','wpe','wpf','wpg','wph'],
            ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
            ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
            ['░ ','▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ '],
            ['▓ ','░ ','▓ ','░ ','▓ ','░ ','▓ ','░ '],
            ['bpa','bpb','bpc','bpd','bpe','bpf','bpg','bph'],
            ['br','bn','bb','bq','bk','bb','bn','br']
        ]
        testGame = cg.Game("foobar")
        self.assertEqual(testGame.board, testBoard)
        
    def test_move_white_pawns(self):
        testGame = cg.Game("foobar")
        # move pawns two space forward
        self.assertTrue(testGame.movePiece('wpa','a4'))
        self.assertTrue(testGame.movePiece('wpb','b4'))
        self.assertTrue(testGame.movePiece('wpc','c4'))
        self.assertTrue(testGame.movePiece('wpd','d4'))
        self.assertTrue(testGame.movePiece('wpe','e4'))
        self.assertTrue(testGame.movePiece('wpf','f4'))
        self.assertTrue(testGame.movePiece('wpg','g4'))
        self.assertTrue(testGame.movePiece('wph','h4'))
        
        # move pawns one space forward
        self.assertTrue(testGame.movePiece('wpa','a5'))
        self.assertTrue(testGame.movePiece('wpb','b5'))
        self.assertTrue(testGame.movePiece('wpc','c5'))
        self.assertTrue(testGame.movePiece('wpd','d5'))
        self.assertTrue(testGame.movePiece('wpe','e5'))
        self.assertTrue(testGame.movePiece('wpf','f5'))
        self.assertTrue(testGame.movePiece('wpg','g5'))
        self.assertTrue(testGame.movePiece('wph','h5'))
        
        testGame = cg.Game("foobar3")
        
        # illegal move when moving pawn two spaces after first move
        
        # move pawns one space forward
        self.assertTrue(testGame.movePiece('wpa','a3'))
        self.assertTrue(testGame.movePiece('wpb','b3'))
        self.assertTrue(testGame.movePiece('wpc','c3'))
        self.assertTrue(testGame.movePiece('wpd','d3'))
        self.assertTrue(testGame.movePiece('wpe','e3'))
        self.assertTrue(testGame.movePiece('wpf','f3'))
        self.assertTrue(testGame.movePiece('wpg','g3'))
        self.assertTrue(testGame.movePiece('wph','h3'))
        
        # move pawns two space forward
        blockPrint()
        self.assertFalse(testGame.movePiece('wpa','a5'))
        self.assertFalse(testGame.movePiece('wpb','b5'))
        self.assertFalse(testGame.movePiece('wpc','c5'))
        self.assertFalse(testGame.movePiece('wpd','d5'))
        self.assertFalse(testGame.movePiece('wpe','e5'))
        self.assertFalse(testGame.movePiece('wpf','f5'))
        self.assertFalse(testGame.movePiece('wpg','g5'))
        self.assertFalse(testGame.movePiece('wph','h5'))
        enablePrint()

if __name__ == '__main__':
   unittest.main()