#%%
data = open("input.txt", "r").read()
code = [string.split() for string in data[:-1].split('\n')]


def execute(code):
    accumulator, i = 0, 0
    executed = []
    while(i < len(code)):
        if(i in executed):
            # print(accumulator, i)
            return False, accumulator
        executed.append(i)
        instr, num = code[i][0], int(code[i][1])
        if(instr == 'acc'):
            accumulator += num
            i += 1
        elif(instr == 'jmp'):
            i += num
        elif(instr == 'nop'):
            i += 1
    return True, accumulator

for i in range(len(code)):
    if(code[i][0] == 'nop'):
        code[i][0] = 'jmp'
        loop, acc = execute(code)
        if(loop):
            print(acc)
            break
        else:
            code[i][0] = 'nop'
    elif(code[i][0] == 'jmp'):
        code[i][0] = 'nop'
        loop, acc = execute(code)
        if(loop):
            print(acc)
            break
        else:
            code[i][0] = 'jmp'
# %%
