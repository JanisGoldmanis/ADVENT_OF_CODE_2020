def part1():
    with open('INPUT/day10.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    lines.sort()

    lines.insert(0, 0)
    lines.append(lines[-1] + 3)

    results = {1: 0, 2: 0, 3: 0}

    for i in range(len(lines) - 1):
        difference = lines[i + 1] - lines[i]

        results[difference] += 1

    print('Multiplied 1 and 3 joltage instances:', results[1] * results[3])


def combination_search(previous_number, leftover_string, dictionary):
    if previous_number in dictionary:
        return dictionary[previous_number]

    if len(leftover_string) == 1:
        return 1

    combinations = 0

    while True:
        if leftover_string[0] - previous_number <= 3:
            next_number = leftover_string.pop(0)
            combinations += combination_search(next_number, leftover_string[:], dictionary)
        else:
            break

    dictionary[previous_number] = combinations
    return combinations


def part2():
    with open('INPUT/day10.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    lines.sort()

    lines.insert(0, 0)
    lines.append(lines[-1] + 3)

    dictionary = {}
    combinations = combination_search(lines.pop(0), lines, dictionary)

    print(combinations)




