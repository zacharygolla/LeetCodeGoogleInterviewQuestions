"""
Given an nxn 2d matix
rotate the image by 90 degrees (clockwise)

example 
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate such that
[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
"""


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(rotateImage(matrix))


def rotateImage(matrix):
    currentRow = 0
    currentColumn = 0

    count = 0
    startingRowLength = len(matrix)
    nextRowLength = startingRowLength
    while(nextRowLength > 1):
        numberOfMovements = nextRowLength - 1
        while (count < len(matrix) * len(matrix)):

            start = matrix[currentRow][currentColumn]

            # take the start value and place it in previous
            #nextvalue, prev = prev, nextvalue
            # do the math to get to the next position
            #nextvalue, prev = prev, nextvalue
            # when the prev is equal to
            currentColumn += 1
            currentRow += 1
            count += 1
        nextRowLength -= 2

    # Take every square and rotate each of the values.
    #   Move into the next square.. If Square size is less than or equal to 1, stop.


if __name__ == "__main__":
    main()
