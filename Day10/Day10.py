#%%
nums = []
with open("input.txt") as data:
    for line in data:
        nums.append(int(line))

nums.sort()
joltage, ones, threes = 0, 0, 1
for num in nums:
    if num - joltage == 1:
        ones += 1
    else:
        threes += 1
    joltage = num
print(ones * threes)
# %%
