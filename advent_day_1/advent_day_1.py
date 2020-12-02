# Open the data and make list
advent_input = open('input.txt', 'r')
a_list = list(advent_input)
advent_input.close()

# Make the list proper
advent_list = [x[:-1] for x in a_list]
advent_list = [int(i) for i in advent_list]

# Look for the 2020 ~ part 1
for i in advent_list:
    for x in advent_list:
        if i + x == 2020:
            print(f'{i} and {x}')
            print(i*x)

# Look for the 2020 ~ part 2
for i in advent_list:
    for x in advent_list:
        for y in advent_list:
            if i + x + y == 2020:
                print(f'{i}, {x}, {y}')
                print(i*x*y)
