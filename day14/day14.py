def masked_value(mask, val, part2):
    b_val = bin(int(val))[2:]
    b_val = (36 - len(b_val)) * '0' + b_val

    for i in range(len(mask)):
        c = b_val[i]
        if not part2 and mask[i] != 'X':
            c = mask[i]
        elif part2 and mask[i] != '0':
            c = mask[i]
        b_val = b_val[:i] + c + b_val[i+1:]

    return replace_x(b_val) if part2 else int(b_val, 2)

def replace_x(b_val):
    if not b_val.count('X'):
        return [b_val]

    v0, v1 = [b_val.replace('X', b, 1) for b in '01']
    return replace_x(v0) + replace_x(v1)

def solve(data, part2):
    mem = {}
    for line in data:
        if line[:4] == 'mask':
            mask = line[7:-1]
            continue

        idx = line[4:line.index(']')]
        val = line[line.index('=')+2:-1]

        if not part2:
            mem[idx] = masked_value(mask, val, part2)
        else:
            for addr in masked_value(mask, idx, part2):
                mem[addr] = int(val)

    return sum(mem[i] for i in mem)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    print(solve(data, False))
    print(solve(data, True))