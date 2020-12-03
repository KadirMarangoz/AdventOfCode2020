#%%
grid = []

with open("input.txt") as data:
    for line in data:
        grid.append(list(line[:-1]))

height, width = len(grid), len(grid[0])
count = 0

pos = 0
for line in grid:
    if(line[pos % width] == '#'):
        line[pos % width] = 'X'
        count += 1
    else: line[pos % width] = 'O'
    pos += 3

print(count)
# %%
