def part1():
    with open('INPUT/day3.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    column = 0
    trees = 0
    pattern_length = len(lines[0])

    for line in lines:
        if line[column] == '#':
            trees += 1
        column += 3
        column = column % pattern_length

    print('Trees encountered:', trees)


def part2():
    with open('INPUT/day3.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    pattern_length = len(lines[0])
    result = 1

    for slope in slopes:
        column = 0
        line_increment = slope[1]
        column_increment = slope[0]
        trees = 0

        for i in range(0, len(lines), line_increment):
            line = lines[i]
            if line[column] == '#':
                trees += 1
            column += column_increment
            column = column % pattern_length

        result *= trees

    print('Trees encountered:', result)
