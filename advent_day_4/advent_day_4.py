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
def passport_check(passport):
    passport_regex_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    check_list = 0
    for check in passport_regex_list:
        if check in passport:
            check_list += 1

    if check_list == 7:
        return True
    else:
        return False


correct_passports = 0

for passport in passport_list:
    print(passport)
    if passport_check(passport) is True:
        correct_passports += 1

print(correct_passports)

print(len(passport_list))
