def get_colors(bag_dictionary, color, color_set):
    found_in = bag_dictionary[color]['found in']
    for color2 in found_in:
        color_set.add(color2)
        get_colors(bag_dictionary, color2, color_set)


def get_count(bag_dictionary, color):
    contains = bag_dictionary[color]['contains']
    result = 0

    if len(contains) == 0:
        return result

    for color2 in contains:
        color2_count = color2['count']
        color2_color = color2['color']

        result += color2_count + color2_count * get_count(bag_dictionary, color2_color)
    return result


def part1():
    with open('INPUT/day7.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    bag_dictionary = {}

    for line in lines:
        parts_1 = line.replace('.', '').split('bags contain')
        color = parts_1[0].strip()

        if color not in bag_dictionary:
            bag_dictionary[color] = {'found in': [], 'contains': []}

        if parts_1[1].strip() != 'no other bags':
            contain_colors = parts_1[1].strip().split(',')

            for containing_color in contain_colors:
                containing_color = containing_color.strip()
                count = int(containing_color.split(' ')[0])
                new_color = ' '.join(containing_color.split(' ')[1:-1])

                if new_color not in bag_dictionary:
                    bag_dictionary[new_color] = {'found in': [], 'contains': []}

                bag_dictionary[color]['contains'].append({'count': count, 'color': new_color})
                bag_dictionary[new_color]['found in'].append(color)

    found_in = set()
    get_colors(bag_dictionary, 'shiny gold', found_in)

    print('Can be found in:', len(found_in))


def part2():
    with open('INPUT/day7.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    bag_dictionary = {}

    for line in lines:
        parts_1 = line.replace('.','').split('bags contain')
        color = parts_1[0].strip()

        if color not in bag_dictionary:
            bag_dictionary[color] = {'found in': [], 'contains': []}

        if parts_1[1].strip() != 'no other bags':
            contain_colors = parts_1[1].strip().split(',')

            for containing_color in contain_colors:
                containing_color = containing_color.strip()
                count = int(containing_color.split(' ')[0])
                new_color = ' '.join(containing_color.split(' ')[1:-1])

                if new_color not in bag_dictionary:
                    bag_dictionary[new_color] = {'found in': [], 'contains': []}

                bag_dictionary[color]['contains'].append({'count': count, 'color': new_color})
                bag_dictionary[new_color]['found in'].append(color)

    count = get_count(bag_dictionary, 'shiny gold')

    print('Contains:', count)
