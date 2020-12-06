advent_input = open('input_6.txt')
advent_data = advent_input.readlines()

enter_list = []
start_element = 0

for line in range(len(advent_data)):
    if advent_data[line] == '\n':
        enter_list.append(line)
enter_list.append((advent_data.index(advent_data[-1]) + 1))

question_list = []

# Combine the passports
for enter in enter_list:
    question_list.append(''.join(advent_data[start_element:enter]))
    start_element = enter + 1


print(question_list)

for word in question_list:
    if "\n" in word:
        question_list[question_list.index(word)] = word.replace("\n", '')

print(question_list)

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

correct_questions = 0

for word in question_list:
    word_correct = 0
    for letter in alfabet:
        if letter in word:
            word_correct += 1
            correct_questions += 1
        print(word_correct, correct_questions)

print(correct_questions)