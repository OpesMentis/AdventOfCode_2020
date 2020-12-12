def next_pos(x, y, wpx, wpy, inst, p2):
    cmd = inst[0]
    val = int(inst[1:])
    chg = {'N': (0,1), 'W': (-1,0), 'S': (0,-1), 'E': (1,0)}

    if cmd in 'NWSE':
        dx, dy = chg[cmd]
        if not p2:
            return x+(dx*val), y+(dy*val), wpx, wpy
        else:
            return x, y, wpx+(dx*val), wpy+(dy*val)

    if cmd == 'F':
        return x+wpx*val, y+wpy*val, wpx, wpy

    L = lambda a, b, rec: (-b,a) if rec==1 else L(-b, a, rec-1)
    R = lambda a, b, rec: (b,-a) if rec==1 else R(b, -a, rec-1)
    if cmd == 'L':
        new_wpx, new_wpy = L(wpx, wpy, val//90)
    else:
        new_wpx, new_wpy = R(wpx, wpy, val//90)
    
    return x, y, new_wpx, new_wpy

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    x1, y1 = x2, y2 = 0, 0
    wpx1, wpy1 = 1, 0
    wpx2, wpy2 = 10, 1

    for inst in data:
        x1, y1, wpx1, wpy1 = next_pos(x1, y1, wpx1, wpy1, inst, False)
        x2, y2, wpx2, wpy2 = next_pos(x2, y2, wpx2, wpy2, inst, True)

    print(abs(x1)+abs(y1))
    print(abs(x2)+abs(y2))