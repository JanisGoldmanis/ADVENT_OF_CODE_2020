def get_row(sequence, min, max):
    if sequence == '':
        return max

    if sequence[0] == 'F' or sequence[0] == 'L':
        return get_row(sequence[1:], min, min + (max-min)//2)

    if sequence[0] == 'B' or sequence[0] == 'R':
        return get_row(sequence[1:], min + (max-min)//2 + 1, max)


def part1():
    with open('INPUT/day5.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    result = 0

    for line in lines:
        row_sequence = line[:7]
        min_row = 0
        max_row = 127

        row = get_row(row_sequence, min_row, max_row)

        min_column = 0
        max_column = 7

        column_sequence = line[7:]

        column = get_row(column_sequence, min_column, max_column)

        seat_id = row * 8 + column

        if seat_id > result:
            result = seat_id

    print('Max ID:', result)


def part2():
    with open('INPUT/day5.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    seats = []

    for line in lines:
        row_sequence = line[:7]
        min_row = 0
        max_row = 127

        row = get_row(row_sequence, min_row, max_row)

        min_column = 0
        max_column = 7

        column_sequence = line[7:]

        column = get_row(column_sequence, min_column, max_column)

        seat_id = row * 8 + column

        seats.append(seat_id)

    seats.sort()

    for i in range(1, len(seats)):
        if seats[i] - seats[i-1] > 1:
            print('Your ID:', seats[i-1] + 1)
            break


