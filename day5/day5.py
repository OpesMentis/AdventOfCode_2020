def get_seat(pass_id):
    row_info = pass_id[:7]
    col_info = pass_id[7:]

    i = 1
    row = 0
    for b in row_info[::-1]:
        row += i * (b == 'B')
        i *= 2

    i = 1
    col = 0
    for b in col_info[::-1]:
        col += i * (b == 'R')
        i *= 2

    seat = row*8 + col
    return seat

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    list_seat = [get_seat(p[:-1]) for p in data]
    print(max(list_seat))

    curr = min(list_seat)
    while curr in list_seat:
        curr += 1

    print(curr)