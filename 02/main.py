def solverProblem1(measurements):
    horizontal = 0
    depth = 0
    for step in measurements:
        action = step.split()[0]
        value = int(step.split()[1])
        if action == "forward":
            horizontal += value
        if action == "down":
            depth += value
        if action == "up":
            depth -= value

    print("Problem 1 answer: " + str(horizontal * depth))


def solverProblem2(measurements):
    horizontal = 0
    depth = 0
    aim = 0
    for step in measurements:
        action = step.split()[0]
        value = int(step.split()[1])
        if action == "forward":
            horizontal += value
            depth += (aim * value)
        if action == "down":
            aim += value
        if action == "up":
            aim -= value

    print("Problem 2 answer: " + str(horizontal * depth))


if __name__ == '__main__':
    with open("./inputs/day2.txt") as file:
        data = [str(line.strip()) for line in file]
    solverProblem1(data)
    solverProblem2(data)
