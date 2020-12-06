import re


def byr_validation(byr):
    if len(byr) != 4:
        return False
    if int(byr) < 1920 or int(byr) > 2002:
        return False

    return True


def iyr_validation(iyr):
    if len(iyr) != 4:
        return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False

    return True


def eyr_validation(eyr):
    if len(eyr) != 4:
        return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False

    return True


def hgt_validation(hgt):
    if 'cm' in hgt:
        height = re.search(r'(\d+)', hgt).group(0)
        if int(height) >= 150 and int(height) <= 193:
            return True
    elif 'in' in hgt:
        height = re.search(r'(\d+)', hgt).group(0)
        if int(height) >= 59 and int(height) <= 76:
            return True

    return False


def hcl_validation(param):
    pattern = re.compile('#[0-9a-f]{6}')
    if(pattern.match(str(param))):
        return True

    return False


def ecl_validation(param):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for v in valid:
        if str(param) == v:
            return True
    return False


def pid_validation(param):
    pattern = re.compile('\d{9}')
    if(pattern.match(param)):
        return True

    return False





input = open("share/d04e01-input", "r")

# print(input.read().split("\n\n"))

passports = input.read().split("\n\n")
counter = 0





for passport in passports:
    # print(passport.replace(' ', '\n'))
    passport = passport.replace(' ', ';').replace('\n', ';')

    # print(passport)

    # print(pp)
    if "byr" in passport and \
            "iyr" in passport and \
            "eyr" in passport and \
            "hgt" in passport and \
            "hcl" in passport and \
            "ecl" in passport and \
            "pid" in passport:
        pp = dict(x.split(':') for x in passport.split(';'))
        # print(pp.get('byr'))
        if byr_validation(pp.get('byr')) and iyr_validation(pp.get('iyr')) and eyr_validation(pp.get('eyr')) and hgt_validation(pp.get('hgt')) and hcl_validation(pp.get('hcl')) and ecl_validation(pp.get('ecl')) and pid_validation(pp.get('pid')):
            counter += 1
            pass

print(counter) # 145