#%%
def isValid(line: str) -> bool:

    rule, password = line.split(": ")
    occurences, key = rule.split()
    first, second = occurences.split("-")
    return (password[int(first)-1] == key) ^ (password[int(second)-1] == key)


valid = 0
count = 0
with open("input.txt") as data: 
    for line in data: 
        count += 1
        valid += isValid(line)
print(valid, count)
# %%
