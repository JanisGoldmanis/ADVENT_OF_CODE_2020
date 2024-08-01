def part1():
    with open('INPUT/day1.txt') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Brute force
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print('Part1:', numbers[i], numbers[j], numbers[i] * numbers[j])

    # To do: implement method that sorts numbers logn, afterwards use pointers from back and front.
    # Should be time complexity should be nlogn


def part2():
    with open('INPUT/day1.txt') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Brute force
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for z in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[z] == 2020:
                    print('Part2:', numbers[i], numbers[j], numbers[z], numbers[i] * numbers[j] * numbers[z])

    # Two pointers will not be enough


