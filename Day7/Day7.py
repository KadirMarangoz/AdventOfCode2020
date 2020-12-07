#%%

dict_ = {}
with open("input.txt") as data:
    for line in data:
        # print(line)
        key, value = line[:-2].replace(" bags", "").replace(" bag", "").split(" contain ")
        # print(value)
        if "no other" in value:
            dict_[key] = {}
            continue
        other_dict = dict([(val[2:], int(val[0])) for val in value.split(", ")])
        dict_[key] = other_dict

def find_gold(dict_, colour):
    if "shiny gold" in dict_[colour]:
        return True
    for key in dict_[colour]:
        if find_gold(dict_, key):
            return True
    return False

def flatten(dict_, colour):
    count = 1
    if len(dict_[colour]) == 0:
        return count

    for key in dict_[colour]:
        count += dict_[colour][key] * flatten(dict_, key)

    return count

print(flatten(dict_, "shiny gold") - 1)







# %%