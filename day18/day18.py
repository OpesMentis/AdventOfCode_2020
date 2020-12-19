def parse_calc(line):
    op = line.strip().replace(' ', '')
    calc = []

    i = 0
    while i < len(op):
        if op[i] in '0123456789':
            calc.append(int(op[i]))
            i += 1
        elif op[i] in '+*':
            calc.append(op[i])
            i += 1
        elif op[i] == '(':
            j = i
            c = 1
            while c > 0:
                j += 1
                if op[j] == '(': c += 1
                elif op[j] == ')': c -= 1
            calc.append(parse_calc(op[i+1:j]))
            i = j+1

    return calc

def part1(op):
    if type(op) == type(0):
        return op
    if len(op) == 1:
        return op[0]

    x1 = part1(op[0])
    x2 = part1(op[2])
    if op[1] == '+':
        return part1([x1+x2]+op[3:])
    else:
        return part1([x1*x2]+op[3:])

def part2(op):
    if type(op) == type(0):
        return op
    if len(op) == 1:
        return op[0]

    if '+' in op:
        idx = op.index('+')
        x1 = part2(op[idx-1])
        x2 = part2(op[idx+1])
        return part2(op[:idx-1]+[x1+x2]+op[idx+2:])

    x1 = part2(op[0])
    x2 = part2(op[2])
    return part2([x1*x2]+op[3:])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    print(sum(part1(parse_calc(l)) for l in data))
    print(sum(part2(parse_calc(l)) for l in data))