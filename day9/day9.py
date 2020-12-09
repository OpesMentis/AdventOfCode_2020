import itertools

def part1(code, pre):
    go_on = True
    i = pre
    while go_on:
        go_on = False
        curr = code[i]
        pool = code[i-pre:i]
        for j,k in itertools.combinations(pool, 2):
            if j+k == curr:
                go_on = True
                break
        i += 1
    return curr

def part2(code, goal):
    s = 0
    c = 0
    l_nb = []
    while s != goal:
        if s < goal:
            s += code[c]
            l_nb.append(code[c])
            c += 1
        if s > goal:
            s -= l_nb.pop(0)
    return min(l_nb) + max(l_nb)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [int(k) for k in f.readlines()]

    print(goal := part1(data, 25))
    print(part2(data, goal))