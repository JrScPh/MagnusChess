# MagnusChess

### Project to code Chess in Python with the goal of implementing an AI chess engine

## ChessFunctions.py
| Function | Parameters | Return | Description |
--- | --- | ---
buildBoard | None | board (2d list) | Creates a 2d list to represent the chess board. Indices are matched to chess board coordinates.
findPiecePos | board (2d list), piece (string) | | Searches for piece in the board and returns the coordinates.
convertNotationToPos | move (string) | Converts chess notation into 2d list coordinates.

## ChessGame.py
| Function | Parameters | Return | Description |
--- | --- | ---
__init__ | self, players (string) | Game | Initializes and returns a new Game object
printBoardBlack | self | None | Prints the board via console from black perspective
printBoardWhite | self | None | Prints the board via console from white perspective
movePiece | self, piece (string), move (string) | Boolean | Matches the given piece and calls relevant move function, updates Game board on success

## ChessMoves.py
| Function | Parameters | Return | Description |
--- | --- | ---
validatePawnMove | board (2d list), piece (string), move (string) | Boolean | Validates pawn moves and captures then returns boolean. En Passant is not yet implemented.
updateBoard | board (2d list), piece (string), move (string) | None | Converts piece position and chess notation to coordinates then updates Game board

## ChessTest.py
| Test | Description |
--- | --- | ---
test_verify_board | Validates board generation for Game
test_move_white_pawns | Validates moves for white pawns. Captures, promotions, and En Passant are not implemented.
