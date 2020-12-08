import re

advent_input = open("input_7.txt")

can_be_contained_in = {}
contains = {}

# Part one reversed tree and Part two normal tree
for line in advent_input.readlines():
    daddy_or_mommy_shark, baby_sharks = line.split(" bags contain ")
    baby_sharkies = []
    baby_shark_regex = re.compile(r'((\w+) (\w+) (bag|bags))')
    baby_shark_regex_2 = re.compile(r'((\d) (\w+) (\w+) (bags|bag))')
    baby_shark = baby_shark_regex.findall(baby_sharks)
    for babies in baby_shark:
        if 'bags' in babies:
            baby_sharkies.append(babies[0].replace(' bags', ''))
        elif 'bag' in babies:
            baby_sharkies.append(babies[0].replace(' bag', ''))

    for baby in baby_sharkies:
        if baby in can_be_contained_in:
            can_be_contained_in[baby].append(daddy_or_mommy_shark)
        else:
            can_be_contained_in[baby] = []
            can_be_contained_in[baby].append(daddy_or_mommy_shark)

    baby_shark_2 = baby_shark_regex_2.findall(baby_sharks)
    for babies in baby_shark_2:
        if daddy_or_mommy_shark in contains:
            contains[daddy_or_mommy_shark].append(babies[0])
        else:
            contains[daddy_or_mommy_shark] = []
            contains[daddy_or_mommy_shark].append(babies[0])

containers = []
new_containers = []


def find_container_for(target):
    if target in can_be_contained_in:
        containers_for_target = can_be_contained_in[target]
        containers.extend(containers_for_target)

        for container_for_target in containers_for_target:
            find_container_for(container_for_target)


def number_of_bags(target):
    if target in contains:
        total = 0
        for bag_inside in contains[target]:
            amount_for_bag_inside, name_of_bag_inside = bag_inside.split(' ', 1)
            if 'bags' in name_of_bag_inside:
                name_of_bag_inside = name_of_bag_inside.replace(' bags', '')
            elif 'bag' in name_of_bag_inside:
                name_of_bag_inside = name_of_bag_inside.replace(' bag', '')
            total += int(amount_for_bag_inside) * (1 + number_of_bags(name_of_bag_inside))
        return total
    else:
        return 0


find_container_for("shiny gold")

for container in containers:
    if container not in new_containers:
        new_containers.append(container)

print(len(new_containers))

print(number_of_bags("shiny gold"))
