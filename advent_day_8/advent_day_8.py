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

while True:
    instruction = instructions[index]
    if instruction not in first_round:
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