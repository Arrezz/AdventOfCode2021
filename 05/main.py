#!/usr/bin/env python3

__author__ = "Arvid Granroth"
__license__ = "GNU GPLv3"


def solverproblem1(data):
    print("Problem 1 solution: ")


def solverproblem2(data):
    print("Problem 2 solution: ")


def main():
    """ Main entry point of the app """
    with open("sample.txt") as file:
        data = [int(line.strip()) for line in file]
    solverproblem1(data)
    solverproblem2(data)


if __name__ == '__main__':
    """ This is executed when run from the command line """
    main()