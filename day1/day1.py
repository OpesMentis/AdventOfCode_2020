def lookingfor2(goal, liste):
    for i in range(len(liste)):
        p = data[i]
        for j in range(i+1, len(data)):
            q = data[j]
            if p + q == goal:
                return p * q

    return -1

def lookingfor3(goal, liste):
    for i in range(len(liste)):
        liste_cp = liste[::]

        p = data[i]
        liste_maj = liste_cp[i+1:]
        r = lookingfor2(goal - p, liste_maj)

        if r > 0:
            return p * r

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [int(i) for i in f.readlines() if i != '\n']


    a = lookingfor2(2020, data)
    b = lookingfor3(2020, data)

    print(a)
    print(b)