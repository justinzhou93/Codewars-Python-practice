def validSolution(board):

    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):
            #vertical check
            vadd += board[j][i]
            #horizontal check
            hadd += board[i][j]
            #numbers check
            if board[i][j] < 1 or board[i][j] > 9:
                print(1)
                return False
        if vadd != 45 or hadd != 45:
            print (2)
            print (vadd)
            print (hadd)
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i*3+k][j*3+l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        print (3)
                        return False
            if gadd != 45:
                return False
    return True