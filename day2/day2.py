def decompose(entry):
    l = entry.split(' ')
    bounds = l[0].split('-')

    lb = int(bounds[0])
    gb = int(bounds[1])
    char = l[1][:-1]
    pw = l[2][:-1]

    return lb, gb, char, pw

def policy_one(entry):
    lb, gb, char, pw = decompose(entry)
    count_char = pw.count(char)
    return lb <= count_char >= lb and count_char <= gb

def policy_two(entry):
    lb, gb, char, pw = decompose(entry)
    return (pw[lb-1] == char) ^ (pw[gb-1] == char)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()

    c_one = 0
    c_two = 0

    for entry in data:
        c_one += policy_one(entry)
        c_two += policy_two(entry)

    print(c_one)
    print(c_two)