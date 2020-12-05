#%%

lines = []
with open("input.txt") as data:
    for line in data:
        lines.append(line[:-1])

location = []
for line in lines:
    numbers = ''.join(map(lambda x: "0" if x in ('L', 'F') else "1", line))
    row, column = numbers[:-3], numbers[-3:]
    row, column = int(row, 2), int(column, 2)
    location.append((row, column))

id_numbers = [row * 8 + column for row, column in location]

print(max(id_numbers))
print(len(id_numbers), 128*8)

front_seats = [i for i in range(8)]
back_seats  = [128 * 8 + i for i in range(8)] 




    # %%

