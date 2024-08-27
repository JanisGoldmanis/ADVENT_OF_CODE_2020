def get_matrix(lines):
    matrix = []
    for line in lines:
        bit_line = []
        for char in line:
            if char == 'L':
                bit_line.append(False)
            if char == '.':
                bit_line.append('.')
        matrix.append(bit_line)
    return matrix


def check_position(row, column, current_matrix, update_matrix):

    # Exit situations that are 'empty'
    if current_matrix[row][column] == '.':
        return True

    empty_count = 0
    filled_count = 0

    # Check each row, except if it's out of bounds
    for i in [row - 1, row, row + 1]:
        if i < 0 or i == len(current_matrix):
            continue

        # Check each column, except if it's out of bounds
        for j in [column - 1, column, column + 1]:
            if j < 0 or j == len(current_matrix[0]):
                continue

            # Don't check for counting the position itself
            if i == row and j == column:
                continue

            # Count instances around
            if current_matrix[i][j] == '.':
                continue
            if not current_matrix[i][j]:
                empty_count += 1
            if current_matrix[i][j]:
                filled_count += 1

    current_situation = current_matrix[row][column]

    # Update if it's currently filled
    if current_situation:
        if filled_count >= 4:
            update_matrix[row][column] = False
            return True
    if not current_situation:
        if filled_count == 0:
            update_matrix[row][column] = True
            return True
    return False


def create_snapshot(matrix):
    result = ''
    for row in matrix:
        for char in row:
            if char == '.':
                result += '.'
                continue
            if char:
                result += '#'
            if not char:
                result += '0'
    return result


def update_current_matrix(current_matrix, update_matrix):
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[0])):
            current_matrix[i][j] = update_matrix[i][j]
    return True


def count_filled_spaces(current_matrix):
    result = 0
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[0])):
            if current_matrix[i][j] is True:
                result += 1
    return result


def print_snapshot(snapshot, row_length):
    j = 0
    for i in range(int(len(snapshot) / row_length)):
        start = j*row_length
        end = (j+1)*row_length
        print(snapshot[start:end])
        j += 1
    print()


def part1():
    with open('INPUT/day11.txt') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    current_matrix = get_matrix(lines)
    update_matrix = get_matrix(lines)

    snapshot = create_snapshot(current_matrix)

    for i in range(100):
        print(i)
        for row in range(len(current_matrix)):
            for column in range(len(current_matrix[0])):
                check_position(row, column, current_matrix, update_matrix)

        update_current_matrix(current_matrix, update_matrix)

        this_snapshot = create_snapshot(current_matrix)

        # print_snapshot(this_snapshot, len(current_matrix[0]))

        if this_snapshot == snapshot:
            break

        else:
            snapshot = this_snapshot

    filled_spaces = count_filled_spaces(current_matrix)
    print(filled_spaces)




