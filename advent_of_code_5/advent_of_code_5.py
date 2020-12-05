# Advent of code day 5

# Open data
advent_input = open('input_5.txt')
advent_data = advent_input.readlines()
advent_data = [x.rstrip() for x in advent_data]


# Create class seat
class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def get_id(seat):
    return seat.row * 8 + seat.column


def create_seat(string):
    start_row = 0
    end_row = 127
    start_column = 0
    end_column = 7
    for letter in string:
        if letter == 'B':
            start_row = int(round(start_row + ((end_row - start_row) / 2)))
        elif letter == 'F':
            end_row = int(end_row - ((end_row - start_row) / 2))
        elif letter == 'R':
            start_column = int(round(start_column + ((end_column - start_column) / 2)))
        elif letter == 'L':
            end_column = int(end_column - ((end_column - start_column) / 2))

        # Decide the row
    if string[6] == 'F':
        row = start_row
    elif string[6] == 'B':
        row = end_row
    else:
        print('INVALID')

    # Decide the column
    if string[9] == 'R':
        column = end_column
    elif string[9] == 'L':
        column = start_column

    else:
        print('INVALID')

    new_seat = Seat(row, column)
    return get_id(new_seat)


# Create the list with seats
seating_list = []

for line in advent_data:
    seat = create_seat(line)
    seating_list.append(seat)

# Part one
seating_list.sort()
print(seating_list[-1])

# Part two

