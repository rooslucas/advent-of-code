# Advent of code day 3

# Get the data
advent_input = open("input_3.txt")
advent_data = advent_input.readlines()
advent_data = [x.rstrip() for x in advent_data]


# Create a function that counts the trees
def check_trees(right, down):
    line_index = 0
    word_index = 0
    trees_count = 0

    while line_index < len(advent_data) - 1:
        word_index += right
        word = word_index % len(advent_data[line_index])
        line_index += down
        line = advent_data[line_index]

        if line[word] == '#':
            trees_count += 1

    return trees_count


# Count the trees for 5 different slopes
slope_1 = check_trees(1, 1)
slope_2 = check_trees(3, 1)
slope_3 = check_trees(5, 1)
slope_4 = check_trees(7, 1)
slope_5 = check_trees(1, 2)

# Get the total amount of trees
total_trees = slope_1 * slope_2 * slope_3 * slope_4 * slope_5
print(total_trees)
