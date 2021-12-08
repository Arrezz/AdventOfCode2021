def solverProblem1(measurements):
    bit_counter_one = 0
    bit_counter_zero = 0
    gamma = ""
    epsilon = ""
    for curr_position in range(0, len(measurements[0])):
        for binary_data in range(0, len(measurements)):
            bit_value = int(list(measurements[binary_data])[curr_position])
            if bit_value == 1:
                bit_counter_one += 1
            else:
                bit_counter_zero += 1
        if bit_counter_zero < bit_counter_one:
            gamma += "1"
        else:
            gamma += "0"
        bit_counter_one = 0
        bit_counter_zero = 0

    for char in gamma:
        if char == "0":
            epsilon += "1"
        else:
            epsilon += "0"


    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print("Problem 1 answer: " + str(gamma * epsilon))


def solverproblem2(measurements):

    bit_counter_one = 0
    bit_counter_zero = 0
    oxygen = ""
    co2 = ""

    measurements_copy = measurements

    for curr_position in range(0, len(measurements[0])):
        for binary_data in range(0, len(measurements)):
            bit_value = int(list(measurements[binary_data])[curr_position])
            if bit_value == 1:
                bit_counter_one += 1
            else:
                bit_counter_zero += 1

        if len(measurements) == 1:
            oxygen = measurements[0]
        if bit_counter_zero > bit_counter_one:
            for potentialdelete in measurements:
                if potentialdelete[curr_position] != "0":
                    measurements.remove(potentialdelete)
        else:
            for potentialdelete in measurements:
                if potentialdelete[curr_position] != "1":
                    measurements.remove(potentialdelete)
        bit_counter_one = 0
        bit_counter_zero = 0

    for curr_position in range(0, len(measurements_copy[0])):
        for binary_data in range(0, len(measurements_copy)):
            bit_value = int(list(measurements_copy[binary_data])[curr_position])
            if bit_value == 1:
                bit_counter_one += 1
            else:
                bit_counter_zero += 1
        if len(measurements_copy) == 1:
            co2 = measurements_copy[0]
        if bit_counter_zero < bit_counter_one:
            for potentialdelete in measurements:
                if potentialdelete[curr_position] != "1":
                    measurements_copy.remove(potentialdelete)
        else:
            for potentialdelete in measurements_copy:
                if potentialdelete[curr_position] != "0":
                    measurements_copy.remove(potentialdelete)
        bit_counter_one = 0
        bit_counter_zero = 0

    int(oxygen, 2)
    int(co2, 2)

    print("Problem 2 answer: " + str(oxygen*co2))


if __name__ == '__main__':
    with open("day3.txt") as file:
        data = [str(line.strip()) for line in file]
    solverProblem1(data)
    solverproblem2(data)
