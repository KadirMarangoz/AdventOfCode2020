import itertools
#%%
data = open("input.txt").read()
instructions = data.splitlines()
# instructions = ['mask = 000000000000000000000000000000X1001X',
# 'mem[42] = 100',
# 'mask = 00000000000000000000000000000000X0XX',
# 'mem[26] = 1']
#%%

def binbits(x):
    """Return binary representation of x with at least n bits"""
    """some func I stole online and modified to specifically make it 36 bits"""
    n = 36
    bits = bin(x).split('b')[1]

    if len(bits) < n:
        return '0' * (n - len(bits)) + bits

#%%
# part 1
# mask = ""
# memory = {}
# for line in instructions:
#     if 'mask' in line: 
#         mask = line.split(' = ')[1]
#     else:
#         adress, value = line.split(' = ')
#         adress = adress[adress.find("[")+1:adress.find("]")]
#         value_bits = binbits(int(value))
#         masked_value = []
#         for i in range(len(mask)):
#             masked_value.append(mask[i]) if mask[i] != 'X' else masked_value.append(value_bits[i])
#         memory[adress] = int(''.join(masked_value), 2)

def get_addr(addr_mask):
    if "X" in addr_mask:
        for r in ("0", "1"):
            yield from get_addr(addr_mask.replace("X", r, 1))
    else:
        yield addr_mask

mask = ""
memory = {}
for line in instructions:
    if 'mask' in line: 
        mask = line.split(' = ')[1]
    else:
        adress, value = line.split(' = ')
        adress = adress[adress.find("[")+1:adress.find("]")]
        
        adress_bits = binbits(int(adress))
        masked_adrr = []
        for i in range(len(mask)):
            masked_adrr.append(mask[i]) if mask[i] != '0' else masked_adrr.append(adress_bits[i])
        # print(adress_bits)
        # print(mask)
        # print("".join(masked_adrr))
        for m in get_addr(''.join(masked_adrr)):
            memory[int(m, 2)] = int(value)

print(sum(memory.values()))
# %%
