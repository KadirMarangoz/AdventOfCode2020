#%%
from string import hexdigits

passports = []
cur_passport = {}
with open("input.txt") as data:
    for line in data:
        if line == "\n":
            passports.append(cur_passport)
            cur_passport = {}
        else:
            pairs = line.split()
            cur_passport.update([i.split(':') for i in pairs])
passports.append(cur_passport)

count = 0
mandatory_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
for passport in passports:
    if not mandatory_keys <= set(passport.keys()):
        continue
    if not 1920 <= int(passport['byr']) <= 2002:
        continue
    if not 2010 <= int(passport['iyr']) <= 2020:
        continue
    if not 2020 <= int(passport['eyr']) <= 2030:
        continue
    if not ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)):
        continue
    if not (passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and all(c in set(hexdigits) for c in passport['hcl'][1:])):
        continue
    if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        continue
    if not (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
        continue
    count += 1
print("count = " + str(count))
# %%
