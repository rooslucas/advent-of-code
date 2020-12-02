# Advent of code day 2

# Open the data and make a dictionary
advent_input = open('input_2.txt', 'r')

password_checks = []


class PasswordCheck:
    def __init__(self, password, min_count, max_count, letter):
        self.password = password
        self.min_count = min_count
        self.max_count = max_count
        self.letter = letter


# Parse input into PasswordChecks
for line in advent_input:
    policy, password = line.strip().split(': ')
    number, letter = policy.split(' ')
    min_count, max_count = number.split('-')
    password_checks.append(PasswordCheck(password, min_count, max_count, letter))

advent_input.close()

# Count the correct passwords Part one
correct_passwords_1 = 0

for password_check in password_checks:
    letter_count = password_check.password.count(password_check.letter)

    if int(password_check.min_count) <= letter_count <= int(password_check.max_count):
        correct_passwords_1 += 1

print(correct_passwords_1)

# Count the correct passwords Part two
correct_passwords_2 = 0

for password_check in password_checks:
    position_a = password_check.password[int(password_check.min_count) - 1]
    position_b = password_check.password[int(password_check.max_count) - 1]

    if position_a == password_check.letter and position_b != password_check.letter:
        print(password_check.letter, position_a, position_b)
        correct_passwords_2 += 1
    elif position_b == password_check.letter and position_a != password_check.letter:
        correct_passwords_2 += 1
        print(password_check.letter, position_b, position_a)

print(correct_passwords_2)
