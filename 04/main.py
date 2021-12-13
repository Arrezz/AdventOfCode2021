#!/usr/bin/env python3

__author__ = "Arvid Granroth"
__license__ = "GNU GPLv3"

def solverProblem1(data, numbers):
    for drawnNumber in numbers:
        for board in boards:
            for row in board:
                for num in row:
                    if num[0] == drawnNumber:
                        num[1] = True
        for board in boards:
            found = True
            for row in board:
                if row[1] == False:
                    found = False

            if found:
                print(boards.index(board))




def solverproblem2(data):
    pass

if __name__ == '__main__':
    with open("sample.txt") as f:
        numbers = [int(n) for n in f.readline().split(",")]
        f.readline()
        boards = []
        board = []
        for line in f:
            if line.strip():
                board.append([[int(n), False] for n in line.split()])
            else:
                boards.append(board)
                board = []

    solverProblem1(boards, numbers)