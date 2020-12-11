advent_input = open('input_9.txt')
advent_data = advent_input.readlines()

advent_data = [int(x.rstrip()) for x in advent_data]

# Part one
end_number = 0

for number in advent_data:
    number_list = []
    index_end = advent_data.index(number)

    if index_end <= 25:
        index_start = 0
    else:
        index_start = advent_data.index(number) - 25

    for i in range(index_start, index_end, 1):
        ii = advent_data[i]
        for x in range(index_start, index_end, 1):
            xx = advent_data[x]
            number_list.append(ii + xx)

    if number not in number_list and index_end > 25:
        end_number = number

# Part two
for number in advent_data:
    count_list = []
    count = 0
    start = advent_data.index(number)
    for i in range(start, len(advent_data), 1):
        count += advent_data[i]
        count_list.append(advent_data[i])
        if count == end_number:
            print(min(count_list) + max(count_list))


