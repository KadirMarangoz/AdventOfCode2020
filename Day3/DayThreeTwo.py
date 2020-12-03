#%%
grid = []

with open("input.txt") as data:
    for line in data:
        grid.append(list(line[:-1]))

height, width = len(grid), len(grid[0])
strategy = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
# strategy = [[1, 2]]

results = []
print(width, height)
for strat in strategy:
    count, x, y = 0, 0, 0
    while(y < height):
        # print(x, y)
        if(grid[y][x] in ['#', 'X']):
            grid[y][x] = 'X'
            count += 1
        else:
            grid[y][x] = 'O'
        
        x = (x + strat[0]) % width
        y += strat[1]
    
    results.append(count)

print(results)
result = 1
for output in results:
    result *= output
print(result)
# %%
