def part1():
    with open('INPUT/day8.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0
    accumulator = 0

    visited = set()
    visited.add(i)

    while True:
        line = lines[i]

        parts = line.split(' ')

        key = parts[0]
        value = int(parts[1])

        if key == 'nop':
            i += 1
            if i in visited:
                break
            visited.add(i)
            continue

        if key == 'acc':
            accumulator += value
            i += 1
            if i in visited:
                break
            visited.add(i)
            continue

        if key == 'jmp':
            i += value
            if i in visited:
                break
            visited.add(i)
            continue

    print('Accumulated:', accumulator)


def part2():
    with open('INPUT/day8.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0

    visited = set()
    visited.add(i)

    while True:
        line = lines[i]

        parts = line.split(' ')

        key = parts[0]
        value = int(parts[1])

        if key == 'nop':
            i += 1
            if i in visited:
                break
            visited.add(i)
            continue

        if key == 'acc':
            i += 1
            if i in visited:
                break
            visited.add(i)
            continue

        if key == 'jmp':
            i += value
            if i in visited:
                break
            visited.add(i)
            continue

    visited_list = list(visited)

    found = False

    while len(visited_list) > 0:
        accumulator = 0
        i = 0
        change_index = visited_list.pop(0)

        visited_instance = set()
        visited_instance.add(i)

        while True:
            line = lines[i]

            parts = line.split(' ')

            key = parts[0]
            if i == change_index:
                if key == 'jmp':
                    key = 'nop'
                elif key == 'nop':
                    key = 'jmp'

            value = int(parts[1])

            if key == 'nop':
                i += 1
                if i >= len(lines):
                    found = True
                    break
                if i in visited_instance:
                    break
                visited_instance.add(i)
                continue

            if key == 'acc':
                i += 1
                accumulator += value
                if i >= len(lines):
                    found = True
                    break
                if i in visited_instance:
                    break
                visited_instance.add(i)
                continue

            if key == 'jmp':
                i += value
                if i >= len(lines):
                    found = True
                    break
                if i in visited_instance:
                    break
                visited_instance.add(i)
                continue

        if found:
            print(f'Accumulator: {accumulator}')
            break





