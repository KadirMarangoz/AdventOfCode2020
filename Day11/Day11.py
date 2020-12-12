#%%
import copy


grid = []
with open("input.txt") as data:
    for line in data:
        grid.append(list(line[:-1]))

#%%
def iterate(start_state):
    curr_state = copy.deepcopy(start_state)
    changes = False
    rows = range(len(start_state))
    columns = range(len(start_state[0]))

    for i in range(len(start_state)):
        for j in range(len(start_state[i])):
            
            if start_state[i][j] == '.':
                continue
            
            count = 0
            if start_state[i][j] == 'L':
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x in rows and y in columns and not(x == i and y == j):
                            if start_state[x][y] == '#': 
                                count += 1
                if count == 0:
                    changes = True
                    curr_state[i][j] = '#'
            elif start_state[i][j] == '#':
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x in rows and y in columns and not(x == i and y == j):
                            if start_state[x][y] == '#': 
                                count += 1
                if count > 3:
                    changes = True
                    curr_state[i][j] = 'L'
    return changes, curr_state

#%%
changes = True
while(changes):
    changes, iteration = iterate(grid)
    grid = iteration

occupations = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            occupations += 1
print(occupations)
# %%

test = ["L.LL.LL.LL",
"LLLLLLL.LL",
"L.L.L..L..",
"LLLL.LL.LL",
"L.LL.LL.LL",
"L.LLLLL.LL",
"..L.L.....",
"LLLLLLLLLL",
"L.LLLLLL.L",
"L.LLLLL.LL"]

test = [list(x) for x in test]
print(test)
_, result = iterate(test) 
print(test)
print(result)

# %%
