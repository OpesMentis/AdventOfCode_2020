with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readlines() if i != '\n']

# Part 1
for p in data:
    q = 2020 - p
    if q in data:
        print(p * q)
        break

# Part 2
for i in range(len(data)):
    for j in range(i+1, len(data)):
        p = data[i]
        q = data[j]
        r = 2020 - p - q

        if r in data:
            print(p*q*r)
            break
