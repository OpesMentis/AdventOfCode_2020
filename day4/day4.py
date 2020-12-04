import re

def parse_info(data):
    fields = {}
    lines = data.split('\n')
    for line in lines:
        infos = line.split(' ')
        for info in infos:
            f = info.split(':')
            fields[f[0]] = f[1]

    return fields

def is_valid_1(info):
    return len(info) == 8 or len(info) == 7 and 'cid' not in info

def is_valid_2(info):
    if not is_valid_1(info):
        return False

    year = r'^([0-9]{4})$'
    height = r'^([0-9]{2,3})(cm|in)$'
    hcl = r'^#[0-9a-f]{6}$'
    ecl = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
    pid = r'^[0-9]{9}$'

    if re.match(year, info['byr']):
        y = int(info['byr'])
        if y < 1920 or y > 2002:
            return False
    else:
        return False

    if re.match(year, info['iyr']):
        y = int(info['iyr'])
        if y < 2010 or y > 2020:
            return False
    else:
        return False

    if re.match(year, info['eyr']):
        y = int(info['eyr'])
        if y < 2020 or y > 2030:
            return False
    else:
        return False

    if (x := re.match(height, info['hgt'])):
        sz = int(x.group(1))
        unit = x.group(2)
        if unit == 'cm' and (sz < 150 or sz > 193):
            return False
        elif unit == 'in' and (sz < 59 or sz > 76):
            return False
    else:
        return False

    if not re.match(hcl, info['hcl']):
        return False

    if not re.match(ecl, info['ecl']):
        return False

    if not re.match(pid, info['pid']):
        return False

    return True

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

    passports = data.split('\n\n')

    count_1, count_2 = 0, 0

    for p in passports:
        info = parse_info(p)
        if is_valid_1(info):
            count_1 += 1

        if is_valid_2(info):
            count_2 += 1

    print(count_1)
    print(count_2)