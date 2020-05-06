# import numpy as np


def get_number_of_islands(binaryMatrix):
    """
    binaryMatrix = [[0,    -1,    0,    -2,    0],
                    [0,    0,    -2,    -2,    -2],
                    [1,    0,    0,    -2,    0],
                    [0,    1,    1,    0,    0],
                    [1,    0,    1,    0,    1] ]
    """

    def process_island(i, j, counter):
        # if i == -1:
        #     i = rows - 1
        # elif i == rows:
        #     i = 0
        #
        # if j == -1:
        #     j = columns - 1
        # elif j == columns:
        #     j = 0

        if binaryMatrix[i][j] == 1:
            binaryMatrix[i][j] = counter
            if i > 0:
                process_island(i - 1, j, counter)
            if i < rows - 1:
                process_island(i + 1, j, counter)
            if j < columns - 1:
                process_island(i, j + 1, counter)
            if j > 0:
                process_island(i, j - 1, counter)

    rows = len(binaryMatrix)
    columns = len(binaryMatrix[0])

    counter = -1

    for i in range(rows):
        for j in range(columns):
            if binaryMatrix[i][j] == 1:
                process_island(i, j, counter)
                counter -= 1

    return (counter + 1) * -1


binaryMatrix = [[0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 1, 0, 1]]

print(get_number_of_islands(binaryMatrix))

print(binaryMatrix)

"""
processIsland(i, j, counter):

binaryMatrix[i][j] = counter;

if right is a valid element processIsland(i+1, j, counter)
if left is a valid element processIsland(i-1, j, counter)
"""





