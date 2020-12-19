import itertools as it

def active_neighbours_1(cubes, pos):
    x0, y0, z0 = pos
    prox = []
    s = 0
    for dx, dy, dz in it.product([-1,0,1], repeat=3):
        if dx == dy == dz == 0:
            continue
        x, y, z = x0+dx, y0+dy, z0+dz
        if (x, y, z) in cubes:
            s += cubes[(x, y, z)] == True
        else:
            prox.append((x, y, z))

    return s, prox

def active_neighbours_2(cubes, pos):
    x0, y0, z0, w0 = pos
    prox = []
    s = 0
    for dx, dy, dz, dw in it.product([-1,0,1], repeat=4):
        if dx == dy == dz == dw == 0:
            continue
        x, y, z, w = x0+dx, y0+dy, z0+dz, w0+dw
        if (x, y, z, w) in cubes:
            s += cubes[(x, y, z, w)] == True
        else:
            prox.append((x, y, z, w))

    return s, prox

def next_cubes(cubes, part2=False):
    cp_cubes = cubes.copy()
    for c in cubes:
        if not part2:
            n, prox = active_neighbours_1(cubes, c)
        else:
            n, prox = active_neighbours_2(cubes, c)
        if cubes[c] and n not in [2, 3]:
            cp_cubes[c] = False
        elif not cubes[c] and n == 3:
            cp_cubes[c] = True

        for x in prox:
            if x not in cp_cubes:
                cp_cubes[x] = False

    return cp_cubes

with open('input.txt', 'r') as f:
    data = f.readlines()

# Part 1

cubes = {}

for i in range(len(data)):
    for j in range(len(data[i])):
        cubes[(i, j, 0)] = data[i][j] == '#'
        for dx, dy, dz in it.product([-1,0,1], repeat=3):
            if dx == dy == dz == 0:
                continue

            x, y, z = i+dx, j+dy, dz
            if (x, y, z) not in cubes:
                cubes[(x, y, z)] = False

for i in range(6):
    cubes = next_cubes(cubes)

print(len([c for c in cubes if cubes[c] == True]))

# Part 2

cubes = {}

for i in range(len(data)):
    for j in range(len(data[i])):
        cubes[(i, j, 0, 0)] = data[i][j] == '#'
        for dx, dy, dz, dw in it.product([-1,0,1], repeat=4):
            if dx == dy == dz == dw == 0:
                continue

            x, y, z, w = i+dx, j+dy, dz, dw
            if (x, y, z, w) not in cubes:
                cubes[(x, y, z, w)] = False

for i in range(6):
    cubes = next_cubes(cubes, True)

print(len([c for c in cubes if cubes[c] == True]))