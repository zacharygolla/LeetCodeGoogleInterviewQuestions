def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(isValidSudoku(board))


def isValidSudoku(board):
    rowCheck = {}
    columnCheck = {}
    boxCheck = {}

    for i in range(9):
        rowCheck.update({i+1: 0})
        columnCheck.update({i+1: 0})
        boxCheck.update({i+1: 0})

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                currentNumber = int(board[i][j])
                box = (i/3) * 3 + j/3
                if columnCheck.get(currentNumber) > 0:
                    return False

                if rowCheck[i] > 0:
                    return True
                if columnCheck[currentNumber] > 0:
                    return True
                if boxCheck[i] > 0:
                    return True

    return False


if __name__ == "__main__":
    main()
