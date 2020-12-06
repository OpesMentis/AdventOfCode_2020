def uniq_ans(resp):
    uniq = set()
    for rs in resp:
        for r in rs:
            uniq.add(r)

    return uniq

def all_ans(resp):
    ans = ''
    for r in resp[0]:
        if all(r in l for l in resp):
            ans += r

    return ans

with open('input.txt', 'r') as f:
    data = f.read()

answers = data.split('\n\n')

tot_1 = 0
tot_2 = 0
for lines in answers:
    resp = lines.split()

    unq = uniq_ans(resp)
    ans = all_ans(resp)
    
    tot_1 += len(unq)
    tot_2 += len(ans)

print(tot_1)
print(tot_2)