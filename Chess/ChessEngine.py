#This file will determine the valid moves for each piece and keep track of the game state. It will also keep a move log to allow for undoing moves and keeping track of the game history.
class ChessGame():
    def __init__(self):
        #The board is a 8x8 2D list, each element of the list has 2 characters, the first character represents the color of the piece, the second character represents the type of the piece
        #The first character is either 'W' for white or 'B' for black
        #The second character is either 'p' for pawn, 'r' for rook, 'n' for knight, 'b' for bishop, 'q' for queen, 'k' for king
        #"--" represents an empty space
        self.board = [
            ['Br', 'Bn', 'Bb', 'Bq', 'Bk', 'Bb', 'Bn', 'Br'],
            ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
            ['Wr', 'Wn', 'Wb', 'Wq', 'Wk', 'Wb', 'Wn', 'Wr']
        ]
        self.wightToMove = True
        self.MoveLog = []

