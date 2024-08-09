def part1():
    with open('INPUT/day2.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    valid = 0

    for line in lines:
        line_parts = line.split(':')

        password = line_parts[1].strip()
        letter = line_parts[0][-1]
        interval = line_parts[0].split(' ')[0]
        split_interval = interval.split('-')
        start = int(split_interval[0])
        end = int(split_interval[1])

        if start <= password.count(letter) <= end:
            valid += 1

    print('Part 1 valid inputs:', valid)


def part2():
    with open('INPUT/day2.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    valid = 0

    for line in lines:
        parts = line.split(':')

        password = parts[1].strip()
        letter = parts[0][-1]
        interval = parts[0].split(' ')[0]
        split_interval = interval.split('-')
        start = password[int(split_interval[0]) - 1]
        end = password[int(split_interval[1]) - 1]

        result = start + end

        if result.count(letter) == 1:
            valid += 1

    print('Part 2 valid inputs:', valid)
