# Advent of code day 2

# Open the data and make a dictionary
advent_input = open('input_2.txt', 'r')

password_checks = []


class PasswordCheck:
    def __init__(self, policy, password):
        self.policy = policy
        self.password = password


for line in advent_input:
    (policy, password) = line.strip().split(':')
    password_checks.append(PasswordCheck(policy, password))

advent_input.close()

# Count the correct passwords
correct_passwords = 0

for password_check in password_checks:
    number, letter = password_check.policy.split(' ')
    letter_count = password_check.password.count(letter)
    min_count, max_count = number.split('-')

    if int(min_count) <= letter_count <= int(max_count):
        correct_passwords += 1

print(correct_passwords)
