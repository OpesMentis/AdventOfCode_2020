with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

get_ticket = lambda line: [int(k) for k in line.split(',')]

ticket_fields = {}
for c in data[0].split('\n'):
    f = c[:c.index(':')]
    r = c[c.index(':')+2:].split(' or ')

    int0 = [int(k) for k in r[0].split('-')]
    r0 = range(int0[0], int0[1]+1)
    int1 = [int(k) for k in r[1].split('-')]
    r1 = range(int1[0], int1[1]+1)

    ticket_fields[f] = [r0, r1]

my_ticket = get_ticket(data[1].split('\n')[1])
nearby_tickets = [get_ticket(l) for l in data[2].split('\n')[1:-1]]

s = 0
correct_tickets = []
for t in nearby_tickets:
    is_corr = True
    for f in t:
        add = True
        for c in ticket_fields:
            if any(f in r for r in ticket_fields[c]):
                add = False
                break
        s += f if add else 0
        is_corr = False if add else is_corr
    if is_corr:
        correct_tickets.append(t)

print(s)

fields = list(ticket_fields.keys())
tickets = [my_ticket] + correct_tickets
poss = [[] for i in fields]

for i in range(len(fields)):
    for j in range(len(fields)):
        i_is_j = True
        for k in range(len(tickets)):
            val = tickets[k][i]
            r0, r1 = ticket_fields[fields[j]]
            if val not in r0 and val not in r1:
                i_is_j = False
                break
        if i_is_j: poss[i].append(fields[j])

changed = True
while changed:
    changed = False
    l = [p[0] for p in poss if len(p) == 1]
    for i in l:
        for j in range(len(poss)):
            if len(poss[j]) > 1 and i in poss[j]:
                poss[j].remove(i)
                changed = True

    l = [f for f in fields if sum(f in p for p in poss) == 1]
    for i in l:
        for j in range(len(poss)):
            if len(poss[j]) > 1 and i in poss[j]:
                poss[j] = [i]
                changed = True

prod = 1
for i in range(len(poss)):
    if poss[i][0].startswith('departure'):
        prod *= my_ticket[i]

print(prod)