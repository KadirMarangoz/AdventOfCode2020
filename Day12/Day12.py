#%%

commands = []
with open("input.txt") as data:
    for line in data:
        commands.append((line[0], line[1:-1]))

coords = 0 + 0j
faceing = 1 + 0j

directions = {'N': 0 + 1j, 'E': 1 + 0j, 'S': 0 - 1j, 'W': -1 + 0j}
for command in commands:
    instruction, value = command[0], int(command[1])
    if instruction == 'F':
        coords += value * faceing
    elif instruction == 'L':
        while(value != 0):
            faceing *= 1j
            value -= 90
    elif instruction == 'R':
        while(value != 0):
            faceing *= -1j
            value -= 90
    else:
        coords += directions[instruction] * value

print(coords)

coords = 0 + 0j
waypoint = 10 + 1j

directions = {'N': 0 + 1j, 'E': 1 + 0j, 'S': 0 - 1j, 'W': -1 + 0j}
for command in commands:
    instruction, value = command[0], int(command[1])
    if instruction == 'F':
        coords += value * waypoint
    elif instruction == 'L':
        while(value != 0):
            waypoint *= 1j
            value -= 90
    elif instruction == 'R':
        while(value != 0):
            waypoint *= -1j
            value -= 90
    else:
        waypoint += directions[instruction] * value


# %%