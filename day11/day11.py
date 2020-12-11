def get_neighbours(grid, i, j, part2):
    li = len(grid)
    lj = len(grid[0])
    s = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x*y==x+y:
                continue
            ii,jj = i+x,j+y
            if part2:
                while 0<=ii<li and 0<=jj<lj and grid[ii][jj]=='.':
                    ii += x
                    jj += y
            if 0<=ii<li and 0<=jj<lj:
                s += grid[ii][jj]=='#'
    return s

def next_grid(grid, part2):
    new_g = [['.' for i in grid[0]] for j in grid]
    c = 5 if part2 else 4
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nb = get_neighbours(grid, i, j, part2)
            if grid[i][j] == '#' and nb >= c:
                new_g[i][j] = 'L'
            elif grid[i][j] == 'L' and nb == 0:
                new_g[i][j] = '#'
            else:
                new_g[i][j] = grid[i][j]
    return new_g

def equal_grid(g1, g2):
    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False
    return True

def solve(grid, part2):
    g = grid
    while True:
        new_g = next_grid(g, part2)
        if equal_grid(g, new_g):
            return sum(sum(i == '#' for i in j) for j in g)
        g = new_g

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    grid = [list(r[:-1]) for r in data]
    print(solve(grid, False))
    print(solve(grid, True))