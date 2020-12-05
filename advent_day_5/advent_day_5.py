# Advent of code day 5

# Open data
advent_input = open('input_5.txt')
advent_data = advent_input.readlines()
advent_data = [x.rstrip() for x in advent_data]


# Create class seat
class Seat:
    def __init__(self, str):
        start_row = 0
        end_row = 127
        start_column = 0
        end_column = 7
        for letter in str:
            if letter == 'B':
                start_row = int(round(start_row + ((end_row - start_row) / 2)))
            elif letter == 'F':
                end_row = int(end_row - ((end_row - start_row) / 2))
            elif letter == 'R':
                start_column = int(round(start_column + ((end_column - start_column) / 2)))
            elif letter == 'L':
                end_column = int(end_column - ((end_column - start_column) / 2))

            # Decide the row
        if str[6] == 'F':
            row = start_row
        elif str[6] == 'B':
            row = end_row
        else:
            print('INVALID')

        # Decide the column
        if str[9] == 'R':
            column = end_column
        elif str[9] == 'L':
            column = start_column

        else:
            print('INVALID')

        self.row = row
        self.column = column

    def id(self):
        return self.row * 8 + self.column


# Create the list with seats
seating_list = [Seat(line).id() for line in advent_data]

# Part one
seating_list.sort()
print(seating_list[-1])

# Part two
for i in range(len(seating_list)):
    if (i + 1) in seating_list and (i - 1) in seating_list and i not in seating_list:
        print(i)

