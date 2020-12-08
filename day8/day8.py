def parse_inst(inst):
    cmd, arg = inst.split()
    return cmd, int(arg)

def exec_code(code):
    acc = 0
    ptr = 0
    l_visited = []
    while True:
        cmd, arg = code[ptr]
        l_visited.append(ptr)

        if cmd == 'acc':
            acc += arg
            ptr += 1
        elif cmd == 'jmp':
            ptr += arg
        else:
            ptr += 1

        if ptr in l_visited:
            normal_end = False
            break
        elif ptr == len(code):
            normal_end = True
            break

    return acc, normal_end

with open('input.txt', 'r') as f:
    data = f.readlines()

l_inst = [parse_inst(i) for i in data]

print(exec_code(l_inst)[0])

i, ok = -1, False
while not ok:
    i += 1
    
    cmd, arg = l_inst[i]
    if cmd == 'acc':
        continue

    if cmd == 'jmp':
        new_inst = ('nop', arg)
        new_code = l_inst[:i] + [new_inst] + l_inst[i+1:]
    else:
        new_inst = ('jmp', arg)
        new_code = l_inst[:i] + [new_inst] + l_inst[i+1:]

    ret, ok = exec_code(new_code)

print(ret)