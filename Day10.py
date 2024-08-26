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
