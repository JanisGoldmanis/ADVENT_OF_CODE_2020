def part1():
    with open('INPUT/day9.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    preamble = 25
    rolling_number_sequence = lines[:preamble]
    number_to_check = 0
    leftover_numbers = lines[preamble:]

    while len(leftover_numbers) > 0:
        number_to_check = leftover_numbers.pop(0)

        i = 0
        j = preamble - 1

        correct_flag = False

        sorted_numbers = rolling_number_sequence[:]
        sorted_numbers.sort()

        while True:
            if i == j:
                break

            first = sorted_numbers[i]
            second = sorted_numbers[j]

            if first + second == number_to_check:
                correct_flag = True
                break

            if first + second > number_to_check:
                j -= 1
                continue

            if first + second < number_to_check:
                i += 1
                continue

        if not correct_flag:
            break

        if correct_flag:
            del rolling_number_sequence[0]
            rolling_number_sequence.append(number_to_check)

    print('Number breaking XMAS:', number_to_check)
    return number_to_check


def part2():
    with open('INPUT/day9.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    number_to_verify = part1()

    i = 0
    j = 1

    while True:
        numbers_to_sum = lines[i:j+1]
        number_sum = sum(numbers_to_sum)

        if number_sum == number_to_verify:
            first = min(numbers_to_sum)
            second = max(numbers_to_sum)
            print(first, second, first + second)
            break

        if number_sum < number_to_verify:
            j += 1
            continue

        if number_sum > number_to_verify:
            i += 1
            continue
