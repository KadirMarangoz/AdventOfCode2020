#%%
def sumIn(og_preamble, num):
    preamble = og_preamble.copy()
    preamble.sort()
    i, j = 0, len(preamble) - 1
    while i != j:
        if preamble[i] + preamble[j] == num:
            return True
        elif preamble[i] + preamble[j] < num:
            i += 1
        elif preamble[i] + preamble[j] > num:
            j -= 1
    return False

nums = []
with open("input.txt") as data:
    for line in data:
        nums.append(int(line))

preamble = nums[:25]
nums = nums[25:]

for num in nums:
    if not sumIn(preamble, num):
        # print(preamble)
        # print(num)
        invalid = num
        break
    preamble.pop(0)
    preamble.append(num)

print(invalid)

for i in range(len(nums)):
    for j in range(i + 1):
        if sum(nums[j:i]) == invalid:
            key = nums[j:i]
            key.sort()
            print(key[0] + key[-1])


# %%
