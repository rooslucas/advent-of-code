advent_input = open('input_6.txt')
advent_data = advent_input.read()
question_list = [line.split('\n') for line in advent_data.split('\n\n')]

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

# Part one
correct_questions = 0

for group in question_list:
    word_correct = 0
    group = ', '.join(group)
    print(group)
    for letter in alfabet:
        if letter in group:
            word_correct += 1
            correct_questions += 1

print(correct_questions)

# Part two
total_correct = 0

for group in question_list:
    for letter in alfabet:
        letter_count = 0
        for person in group:
            if letter in person:
                letter_count += 1

        if letter_count == len(group):
            total_correct += 1

print(total_correct)
