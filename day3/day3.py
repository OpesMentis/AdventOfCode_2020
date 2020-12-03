def nb_trees(data, slope):
    x, y = 0, 0
    count = 0

    while x < len(data):
        char = data[x][y % (len(data[x])-1)]

        if char == '#':
            count += 1

        x += slope[0]
        y += slope[1]

    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    print(nb_trees(data, (1, 3)))

    prod = 1
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    for s in slopes:
        prod *= nb_trees(data, s)

    print(prod)