import re

global rules

def parse_rule(line):
    rule = {}
    colon = line.index(':')
    nb = line[:colon]
    if '"' in line:
        rule['type'] = 'letter'
        rule['cont'] = line[-2]
        return nb, rule

    if '|' not in line:
        rule['type'] = 'order'
        rule['cont'] = line[colon+2:].split()
        return nb, rule

    rule['type'] = 'or'
    rule['cont'] = [i.split() for i in line[colon+2:].split(' | ')]
    return nb, rule

def get_words(idx):
    r = rules[idx]
    if r['type'] == 'letter':
        return r['cont']

    if r['type'] == 'order':
        return ''.join(f'({get_words(i)})' for i in r['cont'])

    x = []
    for j in r['cont']:
        x.append(''.join(f'{get_words(i)}' for i in j))

    return '(' + '|'.join(x) + ')'

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        raw_rules, raw_words = f.read().split('\n\n')

    rules = {}
    for rule in raw_rules.split('\n'):
        nb, r = parse_rule(rule)
        rules[nb] = r

    words = raw_words.split('\n')

    rex = '^' + get_words('0') + '$'
    print(sum(1 for w in words if re.match(rex, w)))

    rec = 10
    rules['8'] = {'type': 'or', 'cont': [['42']*i for i in range(1,rec)]}
    rules['11'] = {'type': 'or', 'cont': [['42']*i + ['31']*i for i in range(1,rec)]}

    rex = '^' + get_words('0') + '$'
    print(sum(1 for w in words if re.match(rex, w)))
