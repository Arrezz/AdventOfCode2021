#Only problem 1 for now!

def solver(measurements):
    increase = 0

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increase += 1

    print(increase)


if __name__ == '__main__':
    with open("./inputs/day1.txt") as file:
        data = [int(line.strip()) for line in file]
    solver(data)
