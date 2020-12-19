with open('input.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]

i = len(data)
while i < 30000000:
    curr = data[-1]
    if curr not in data[:-1]:
        data.append(0)

    else:
        data.append(data[-2::-1].index(curr)+1)

    i += 1

print(data[-1])