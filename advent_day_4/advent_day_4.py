import re

advent_input = open('input_4.txt')
advent_data = advent_input.readlines()

line = advent_data[0]

enter_list = []
start_element = 0

for line in range(len(advent_data)):
    if advent_data[line] == '\n':
        enter_list.append(line)

passport_list = []

# Combine the passports
for enter in enter_list:
    passport_list.append(''.join(advent_data[start_element:enter]))
    start_element = enter + 1

print(passport_list)


# Create the regexes
# byr:2010 pid:#1bb4d8 eyr:2021 hgt:186cm iyr:2020 ecl:grt
def passport_check_part_one(passport):
    passport_regex_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    check_list = 0
    for check in passport_regex_list:
        if check in passport:
            check_list += 1

    return check_list == 7


def passport_check_part_two(passport):
    byr = re.compile(r'byr:(19[23456789]\d|200[012])')
    iyr = re.compile(r'iyr:(20[1]\d|2020)')
    eyr = re.compile(r'eyr:(20[2]\d|2030)')
    hcl = re.compile(r'hcl:#[0-9a-f]{6}')
    ecl = re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)')
    pid = re.compile(r'pid:\d{9}')
    hgt = re.compile(r'59in|6\din|7[0123456]in|1[5678]\dcm|19[01234]cm') # TODO: Check hgt prefix

    passport_regex_list = [byr, iyr, eyr, hcl, ecl, pid, hgt]
    for check in passport_regex_list:
        if check.search(passport) is None:
            return False

    return True


correct_passports_1 = 0
correct_passports_2 = 0

# Check part one
for passport in passport_list:
    if passport_check_part_one(passport):
        correct_passports_1 += 1

print(correct_passports_1)

# Check part two
for passport in passport_list:
    if passport_check_part_two(passport) and passport_check_part_one(passport):
        correct_passports_2 += 1

print(correct_passports_2)
