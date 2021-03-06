#!/usr/bin/env python3

__author__ = "Arvid Granroth"
__license__ = "GNU GPLv3"

def solverProblem1(measurements):
    increase = 0

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increase += 1

    print("Problem 1 answer: " + increase)


def solverProblem2(measurements):
    increase = 0

    for i in range(2, len(measurements) - 1):
        if (measurements[i - 2] + measurements[i - 1] + measurements[i]) < (
                measurements[i - 1] + measurements[i] + measurements[i + 1]):
            increase += 1

    print("Problem 2 answer: " + increase)


if __name__ == '__main__':
    with open("./inputs/day1.txt") as file:
        data = [int(line.strip()) for line in file]
    solverProblem1(data)
    solverProblem2(data)
