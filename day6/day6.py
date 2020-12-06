def uniq_ans(resp):
    uniq = set()
    for rs in resp:
        for r in rs:
            uniq.add(r)

    return uniq

def all_ans(resp):
    ans = ''
    for r in resp[0]:
        ans += r * all(r in l for l in resp)

    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

    answers = data.split('\n\n')

    tot_1 = 0
    tot_2 = 0
    for lines in answers:
        resp = lines.split()
        tot_1 += len(uniq_ans(resp))
        tot_2 += len(all_ans(resp))

    print(tot_1)
    print(tot_2)