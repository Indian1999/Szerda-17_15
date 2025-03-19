# 8*8 as mátrix tele 0-val
chess_board = [[0 for j in range(8)] for i in range(8)]

def hits_another_queen(i,j):
    """Eldönti, hogy ezen a cellán lévő királynő, üt-e egy másikat."""
    return False

def is_valid_chess_board():
    """
    Igazat ad vissza, ha egy királynő sem üti egymást, egyébként hamissal tér vissza.
    """
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            if chess_board[i][j] == 1:
                invalid = hits_another_queen(i,j)
                if invalid:
                    return False
    return True
                
for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    for f in range(8):
                        for g in range(8):
                            for h in range(8):
                                chess_board[0][a] = 1
                                chess_board[1][b] = 1
                                chess_board[2][c] = 1
                                chess_board[3][d] = 1
                                chess_board[4][e] = 1
                                chess_board[5][f] = 1
                                chess_board[6][g] = 1
                                chess_board[7][h] = 1
                                is_valid_chess_board()