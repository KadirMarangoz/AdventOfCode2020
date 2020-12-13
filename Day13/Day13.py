#%%

with open("input.txt") as data:
    for i, line in enumerate(data):
        if i == 0:
            departure = int(line)
        else: 
            input = line.split(',')

busses = [int(x) for x in input if x != 'x']
closest_dep = [(((departure // x) + 1) * x - departure, x) for x in busses]
wait, bus_id = min(closest_dep, key = lambda t: t[0])
print(wait * bus_id)
# %%

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

n = []
a = []
busses = input
for i, bus in enumerate(busses):
    if bus == 'x':
        continue
    bus = int(bus)
    n.append(bus)
    a.append((-i) % bus)
print(chinese_remainder(n, a))
# %%
