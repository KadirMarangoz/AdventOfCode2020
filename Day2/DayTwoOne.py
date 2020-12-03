def isValid(line: str) -> bool:

    rule, password = line.split(": ")
    occurences, key = rule.split()
    least, most = occurences.split("-")
    return password.count(key) <= int(most) and password.count(key) >= int(least)


valid = 0
count = 0
with open("input.txt") as data: 
    for line in data: 
        count += 1
        valid += isValid(line)
print(valid, count)