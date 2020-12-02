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
    policy, password = line.strip().split(':')
    number, letter = policy.split(' ')
    min_count, max_count = number.split('-')
    password_checks.append(PasswordCheck(password, min_count, max_count, letter))

advent_input.close()

# Count the correct passwords
correct_passwords = 0

for password_check in password_checks:
    letter_count = password_check.password.count(password_check.letter)

    if int(password_check.min_count) <= letter_count <= int(password_check.max_count):
        correct_passwords += 1

print(correct_passwords)
