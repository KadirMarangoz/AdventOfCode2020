# %%
from re import L

from numpy.core.getlimits import _register_type


class KaMa:
    def __init__(self, value):
        self.value = value
    def __add__(self, b):
        return KaMa(self.value * b.value)
    def __sub__(self, b):
        return KaMa(self.value + b.value)
    def __mul__(self, b):
        return KaMa(self.value + b.value)

part2 = False
with open("input.txt") as f:
    inp = f.read()
# with open("example_input.txt") as f:
#     inp = f.read()

lines = [line for line in inp.split("\n") if line]
t = 0
digits = [i for i in range(10)]
for line in lines:
    for digit in digits:
        line = line.replace(f"{digit}", f"T({digit})")
    line = line.replace("+", "#")
    line = line.replace("*", "+")
    line = line.replace("#", "*")
    t += eval(line, {"T": KaMa}).value
print(t)

# %%
class K:
    def __init__(self, value):
        self.value = value
    def __add__(self, b):
        return K(self.value + b.value)

print((K(5) + K(3)).value)

def add(self, b):
    return K(self.value * b.value)

K.__add__ = add
print((K(5) + K(3)).value)

# %%
