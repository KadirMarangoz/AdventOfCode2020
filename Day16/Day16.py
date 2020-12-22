#%%
with open("input.txt") as data:
    i = 0
    rules, nearby_tick = {}, []
    for line in data:
        if "your ticket" in line or "nearby ticket" in line:
            i += 1
            continue
        if i == 0:
            field = line.split(': ')[0]
            constraints = [(int(p), int(q)) for (p, q) in zip(*[x.split('-') for x in line.split(': ')[1].split(' or ')])]
            rules[field] = constraints
        if i == 1:
            your_tick = [int(x) for x in line.split(',')]
        if i == 2:
            nearby_tick.append([int(x) for x in line.split(',')])

# %%
valid_nums = []
for key in rules:
    x, p = rules[key][0]
    y, q = rules[key][1]
    valid_nums.append(range(x, y+1))
    valid_nums.append(range(p, q+1))

# %%
# part 1
# invalid_nums = []
# for ticket in nearby_tick:
#     for i, num in enumerate(ticket):
#         valid = False
#         for _range in valid_nums:
#             if num in _range:
#                 valid = True
#                 break
#         if not valid: 
#             invalid_nums.append(num)

# %%
# part 2
for i, ticket in enumerate(nearby_tick):
    for num in ticket:
        valid = False
        for _range in valid_nums:
            if num in _range:
                valid = True
                break
        if not valid: 
            nearby_tick.pop(i)

possible = {name: set(i for i in range(20)) for name in rules}
for ticket in nearby_tick:
    for key in rules:
        for i in range(20):
            x, p = rules[key][0]
            y, q = rules[key][1]          
            valid = ticket[i] in range(x, y+1) or ticket[i] in range(p, q+1)
            if not valid:
                possible[key].remove(i)

mappings = {}
for i in range(20):
    for key in possible:
        if len(possible[key]) == 1:
            elem = possible[key].pop()
            mappings[key] = elem
            for _key in possible:
                if elem in possible[_key]:
                    possible[_key].remove(elem)

product = 1
for key in mappings:
    if 'departure' in key:
        product *= mappings[key]
print(product)
# %%
