def get_adj_matrix(adapters):
    l = [0] + adapters + [max(adapters)+3]
    r = range(len(l))
    m = [[0 for i in r] for j in r]

    for i in r:
        for j in r:
            m[i][j] = int(0 < l[j]-l[i] < 4)
    return m

def prod_sq_matrix(m, n):
    r = range(len(m))
    p = [[0 for i in r] for j in r]

    for i in r:
        for j in r:
            p[i][j] = sum(m[i][k]*n[k][j] for k in r)
    return p

def part1(adapters):
    j = 0
    diff_1 = 0
    diff_3 = 0

    for a in adapters:
        if a - j == 1:
            diff_1 += 1
        else:
            diff_3 += 1
        j = a
    
    return diff_1 * (diff_3+1)

def part2(adapters):
    '''Method using the adjacency matrix'''
    m = get_adj_matrix(adapters)
    lg = len(adapters) + 1

    paths = prod_sq_matrix(m, m)
    s = 0
    for i in range(lg):
        paths = prod_sq_matrix(paths, m)
        s += paths[0][-1]

    return s

def part2_alt(adapters):
    '''Faster method using dynamic programming'''
    l = [0] + adapters + [max(adapters)+3]
    d = [0] * (max(l)+1)
    d[0] = 1

    for i in l[1:]:
        d[i] = sum(d[max(0,i-3):i])

    return d[-1]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = sorted([int(k) for k in f.readlines()])

    print(part1(data))
    print(part2(data))
    print(part2_alt(data))