def part1():
    with open('INPUT/day6.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    group = []
    result = 0

    for i in range(len(lines) + 1):
        if i < len(lines):
            line = lines[i]
        if line == '' or i == len(lines):
            questions = set()
            for person in group:
                for answer in person:
                    questions.add(answer)
            result += len(questions)
            group = []
        if line != '':
            group.append(line)

    print('Unique question sum of each group:', result)


def part2():
    with open('INPUT/day6.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    group = []
    result = 0

    for i in range(len(lines) + 1):
        if i < len(lines):
            line = lines[i]
        if line == '' or i == len(lines):
            questions = set()
            for person in group:
                for answer in person:
                    questions.add(answer)

            all_yes = set()

            for question in questions:
                valid_question = True
                for person in group:
                    if question not in person:
                        valid_question = False
                if valid_question:
                    all_yes.add(question)

            result += len(all_yes)
            group = []

        if line != '':
            group.append(line)

    print('Unique question sum of each group:', result)