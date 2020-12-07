def contain_color(c_ext, c_in, info):
    if c_in in info[c_ext]:
        return True
    if info[c_ext] == []:
        return False

    return any(contain_color(b, c_in, info) for b in info[c_ext])

def count_bags(color, info):
    s = 0
    if info[color] == []:
        return 0

    for b in info[color]:
        q = info[color][b]
        s += q + q * count_bags(b, info)

    return s

def parse_info(line):
    words = line.split()
    ext_color = ' '.join(words[:2])
    l_bags = {}
    nb_bags = len(words[4:]) // 4

    for b in range(nb_bags):
        col = ' '.join(words[5+b*4:7+b*4])
        nb = int(words[4+b*4])
        l_bags[col] = nb

    return {ext_color: l_bags}

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    info = {}
    for l in data:
        info.update(parse_info(l))

    print(sum(contain_color(c, 'shiny gold', info) for c in info))
    print(count_bags('shiny gold', info))