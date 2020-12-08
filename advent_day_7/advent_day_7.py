import re

advent_input = open("input_7.txt")

can_be_contained_in = {}

for line in advent_input.readlines():
    daddy_or_mommy_shark, baby_sharks = line.split(" bags contain ")
    baby_sharkies = []
    baby_shark_regex = re.compile(r'((\w+) (\w+) (bag|bags))')
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

print(can_be_contained_in)


containers = []
new_containers = []

def find_container_for(target):
    if target in can_be_contained_in:
        containers_for_target = can_be_contained_in[target]
        containers.extend(containers_for_target)
        for container_for_target in containers_for_target:
            find_container_for(container_for_target)


find_container_for("shiny gold")

for container in containers:
    if container not in new_containers:
        new_containers.append(container)

print(len(new_containers))