def part1():
    with open('INPUT/day4.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_count = 0
    line_count = len(lines)

    temp_parts = []

    for i in range(line_count):
        line = lines[i]
        temp_parts += line.split(' ')

        if i != line_count - 1:
            if lines[i + 1] != '':
                continue

        found_keys = []
        for part in temp_parts:
            found_keys.append(part.split(':')[0])

        is_valid = True

        for key in keys:
            if key in found_keys:
                continue
            else:
                is_valid = False

        if is_valid:
            valid_count += 1

        temp_parts = []

    print('Valid passports:', valid_count)

def part2():
    with open('INPUT/day4.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_count = 0
    line_count = len(lines)

    temp_parts = []
    passports_with_all_values = []

    for i in range(line_count):
        line = lines[i]
        temp_parts += line.split(' ')

        if i != line_count - 1:
            if lines[i + 1] != '':
                continue

        found_keys = []
        passport = {}
        for part in temp_parts:
            if part == '':
                continue
            key = part.split(':')[0]
            value = part.split(':')[1]
            found_keys.append(key)

            passport[key] = value

        all_keys_found = True

        for key in keys:
            if key in found_keys:
                continue
            else:
                all_keys_found = False

        if all_keys_found:
            passports_with_all_values.append(passport)

        temp_parts = []

    for passport in passports_with_all_values:
        all_key_values_valid = True
        try:
            # Check byr
            year = int(passport['byr'])
            if not 1920 <= year <= 2002:
                all_key_values_valid = False

            # Check iyr
            year = int(passport['iyr'])
            if not 2010 <= year <= 2020:
                all_key_values_valid = False

            # Check eyr
            year = int(passport['eyr'])
            if not 2020 <= year <= 2030:
                all_key_values_valid = False

            # Check hgt
            height_string = passport['hgt']
            if height_string[-2:] == 'cm':
                height = int(height_string[:-2])
                if not 150 <= height <= 193:
                    all_key_values_valid = False
            elif height_string[-2:] == 'in':
                height = int(height_string[:-2])
                if not 59 <= height <= 76:
                    all_key_values_valid = False
            else:
                all_key_values_valid = False

            # Check hcl
            hair_color = passport['hcl']
            if not hair_color[0] == '#':
                all_key_values_valid = False

            if not len(hair_color) == 7:
                all_key_values_valid = False

            if not hair_color[1:].isalnum():
                all_key_values_valid = False

            # Check ecl
            color = passport['ecl']
            if color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                all_key_values_valid = False

            # Check pid
            id = passport['pid']
            if len(id) != 9:
                all_key_values_valid = False

            if not id.isdigit():
                all_key_values_valid = False

        except ValueError:
            all_key_values_valid = False

        if all_key_values_valid:
            valid_count += 1


    print('Valid passports:', valid_count)



