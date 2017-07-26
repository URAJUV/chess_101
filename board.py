import sys
import argparse,json

map_from_alpha_to_index = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
map_from_index_to_alpha = { 0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--piece", help="chess piece name: ex- rook, knight, pawn etc")
parser.add_argument("-l", "--location", help="chess notation string: ex- E4, D6 etc")
args = parser.parse_args()

piece = args.piece.strip().lower()
location = args.location.strip()


def make_board_layout():
    chessboard = [[1] * 8 for i in xrange(8)]
    print (chessboard)
    return chessboard

def get_knightMoves(pos, chessBoard):
    """ A function(positionString, board) that returns the all possible moves
        of a knight stood on a given position
    """
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
       temp = chessBoard[i + 1][j + 2]
       solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass
    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

def get_rookMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []

    # Compute the moves in Rank
    for j in xrange(8):
        if j != column:
            solutionMoves.append((row, j))

    # Compute the moves in File
    for i in xrange(8):
        if i != row:
            solutionMoves.append((i, column))

    solutionMoves = ["".join([map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in solutionMoves]
    solutionMoves.sort()
    return solutionMoves

def get_bishopMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    # Compute the moves in diagonal
    for i in xrange(8):
        # Skip the place where bishop is at present
            if (i != 0):
                solutionMoves.append((row + i , column + i ))
                solutionMoves.append((row + i , column - i ))
                solutionMoves.append((row - i , column + i ))
                solutionMoves.append((row - i , column - i ))
   
    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[0] < 8 and i[1] >=0 and i[1] < 8]
    solutionMoves = ["".join([map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    solutionMoves.sort()
    return solutionMoves
def get_queenMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    solutionMoves.append(get_rookMoves(pos, chessBoard)+get_bishopMoves(pos, chessBoard))
    solutionMoves.sort()
    return solutionMoves

def get_kingMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = map_from_alpha_to_index[column]
    solutionMoves = []
    # Compute the moves for king
    # Skip the place where king is at present
    solutionMoves.append((row + 1 , column ))
    solutionMoves.append((row - 1 , column ))
    solutionMoves.append((row , column + 1 ))
    solutionMoves.append((row , column - 1 ))

    solutionMoves.append((row + 1 , column + 1 ))
    solutionMoves.append((row - 1 , column - 1))
    solutionMoves.append((row + 1 , column - 1 ))
    solutionMoves.append((row - 1 , column + 1 ))
    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[0] < 8 and i[1] >=0 and i[1] < 8]
    solutionMoves = ["".join([map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    solutionMoves.sort()
    return solutionMoves

chessBoard = make_board_layout()
# According to the type of piece adjust function
if (piece == "rook"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": get_rookMoves(location, chessBoard)})
elif (piece == "knight"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": get_knightMoves(location, chessBoard)})
elif (piece == "bishop"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": get_bishopMoves(location, chessBoard)})
elif (piece == "queen"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": get_queenMoves(location, chessBoard)})
elif (piece == "king"):
    print json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": get_kingMoves(location, chessBoard)})


