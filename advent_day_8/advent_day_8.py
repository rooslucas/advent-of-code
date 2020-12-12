advent_input = open('input_8.txt')
advent_data = advent_input.readlines()
instructions = []


class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument


for line in advent_data:
    operation, argument = line.strip().split(' ')
    instructions.append(Instruction(operation, argument))

advent_input.close()

index = 0
accumulator = 0
first_round = []
index_list = []

# Part one
while True:
    instruction = instructions[index]
    if instruction not in first_round:
        index_list.append(index)
        if instruction.operation == 'acc':
            accumulator += int(instruction.argument)
            index += 1
            first_round.append(instruction)
        elif instruction.operation == 'jmp':
            index += int(instruction.argument)
            first_round.append(instruction)
        elif instruction.operation == 'nop':
            index += 1
            first_round.append(instruction)
    else:
        break

print(accumulator)
print(len(index_list))
print(len(first_round))

# Part two

jmp_nop = []


for index in index_list:
    if instructions[index].operation != 'jmp' or instructions[index].operation != 'nop':
        index_list.remove(index)

print(len(index_list))

for attempt in index_list:
    while True:
        index = 0
        accumulator_2 = 0
        index_list_2 = []
        if instructions[attempt].operation == 'jmp':
            instructions[attempt].operation = 'nop'
        elif instructions[attempt].operation == 'nop':
            instructions[attempt].operation = 'jmp'
        while True:
            instruction = instructions[index]
            if index == 612:
                break
            elif index in index_list_2:
                break
            else:
                index_list_2.append(index)
                if instruction.operation == 'acc':
                    accumulator_2 += int(instruction.argument)
                    index += 1
                elif instruction.operation == 'jmp':
                    index += int(instruction.argument)
                elif instruction.operation == 'nop':
                    index += 1
        if index == 612:
            break
        if instructions[attempt].operation == 'jmp':
            instructions[attempt].operation = 'nop'
        elif instructions[attempt].operation == 'nop':
            instructions[attempt].operation = 'jmp'

print(accumulator_2)
