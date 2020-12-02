# Advent of code day 2

# Open the data and make a dictionary
advent_input = open('input_2.txt', 'r')
policy_list = []
password_list = []

for line in advent_input:
    (policy, password) = line.strip().split(':')
    policy_list.append(policy)
    password_list.append(password)

advent_input.close()

# Count the correct passwords
correct_passwords = 0

for i in range(len(password_list)):
    password = password_list[i]
    policy = policy_list[i]

    number, letter = policy.split(' ')

    letter_count = password.count(letter)
    min_count, max_count = number.split('-')

    if int(min_count) <= letter_count <= int(max_count):
        correct_passwords += 1

print(correct_passwords)
