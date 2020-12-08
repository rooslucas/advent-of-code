import re

advent_input = open("text.txt")
# baggage = [line.split(' bags contain ') for line in advent_data.split('\n')]

can_be_contained_in = {}

for line in advent_input.readlines():
    daddy_or_mommy_shark, baby_sharks = line.split(" bags contain ")
    baby_sharkies = []
    baby_shark_regex = re.compile(r'((\w+) (\w+) (bag|bags))')
    baby_shark = baby_shark_regex.findall(baby_sharks)
    for babies in baby_shark:
        baby_sharkies.append(babies[0].replace(' bags', ''))

    for baby in baby_sharkies:
        if baby in can_be_contained_in:
            can_be_contained_in[baby].append(daddy_or_mommy_shark)
        else:
            can_be_contained_in[baby] = []
            can_be_contained_in[baby].append(daddy_or_mommy_shark)

print(can_be_contained_in)
