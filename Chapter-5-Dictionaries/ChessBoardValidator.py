#a valid board should have:
    #spaces MAX 1a to 8h (no 9z for instance)
    #pieces must start with 'w' or 'b' (to denote black or white)
    #each player can have max 16 pieces, 8 of which can be pawns

def validBoard(Board):
    valid_x = ['1', '2', '3', '4', '5', '6', '7', '8']
    valid_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    valid_pieces = ['pawn', 'knight,' 'bishop', 'rook', 'king', 'queen']
    valid_len = 64

    #check for correct number of spaces
    if len(Board) != valid_len:
        return False

    #check for valid spaces
    for space in Board.keys():
        if len(space) != 2:
            return False
            break
        if space[0] not in valid_x:
            return False
            break
        elif space[1] not in valid_y:
            return False
            break

    wpawn = 0
    bpawn = 0
    wTotal = 0
    bTotal = 0

    #check if piece is valid
    for piece in Board.values():
        if piece == ' ':
            continue
        if piece[0] != 'b' and piece[0] != 'w':
            return False
            break
        elif piece[1:] not in valid_pieces:
            return False
            break

        #if piece is valid, add to count for total numbers per team
        if piece[0] == 'b':
            bTotal += 1
        if piece == 'bpawn':
            bpawn += 1
        if piece[0] == 'w':
            bTotal += 1
        if piece == 'wpawn':
            bpawn += 1

    #at most 8 pawns and 16 pieces per color
    if bTotal > 16 or bpawn > 8 or wTotal > 16 or wpawn > 8:
        return False
    #there has to be one king on each team
    elif 'bking' not in Board.values():
        return False
    elif 'wking' not in Board.values():
        return False
    else:
        return True

Board = {'1a': 'bpawn', '2a': 'bpawn', '3a': 'bpawn', '4a': 'bpawn', '5a': 'bpawn', '6a': 'bpawn', '7a': 'bpawn', '8a': 'bpawn',
'1b': ' ', '2b': ' ', '3b': ' ', '4b': ' ', '5b': ' ', '6b': ' ', '7b': ' ', '8b': ' ',
'1c': ' ', '2c': ' ', '3c': ' ', '4c': ' ', '5c': ' ', '6c': ' ', '7c': ' ', '8c': ' ',
'1d': ' ', '2d': 'bking', '3d': ' ', '4d': ' ', '5d': ' ', '6d': ' ', '7d': ' ', '8d': ' ',
'1e': ' ', '2e': ' ', '3e': 'wking', '4e': ' ', '5e': ' ', '6e': ' ', '7e': ' ', '8e': ' ',
'1f': ' ', '2f': ' ', '3f': ' ', '4f': ' ', '5f': ' ', '6f': ' ', '7f': ' ', '8f': ' ',
'1g': ' ', '2g': ' ', '3g': ' ', '4g': ' ', '5g': ' ', '6g': ' ', '7g': ' ', '8g': ' ',
'1h': ' ', '2h': ' ', '3h': ' ', '4h': ' ', '5h': ' ', '6h': ' ', '7h': ' ', '8h': ' '}


print(validBoard(Board))
