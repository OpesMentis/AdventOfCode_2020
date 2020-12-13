with open('input.txt', 'r') as f:
    ts = int(f.readline())
    ids = [int(i) if i != 'x' else 0 for i in f.readline().split(',')]

min_dpt = ts * 2
for i in ids:
    if i == 0:
        continue
    if ts % i == 0:
        depart = ts
    else:
        depart = ((ts // i)+1) * i

    if depart < min_dpt:
        min_dpt = depart
        min_id = i

print(min_id * (min_dpt - ts))

s = 0
p = 1
for i in ids:
    p *= i if i != 0 else 1

for t in range(len(ids)):
    n = ids[t]
    if n == 0:
        continue
    n_ = p // n
    v = 1
    while (v * n_) % n != 1:
        v += 1
    s += (n-t) * v * n_

print(s % p)
