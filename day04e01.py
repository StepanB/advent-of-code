input = open("share/d04e01-input", "r")

# print(input.read().split("\n\n"))

passports = input.read().split("\n\n")
counter = 0
for passport in passports:
    # print(passport.replace(' ', '\n'))
    if "byr" in passport and \
            "iyr" in passport and \
            "eyr" in passport and \
            "hgt" in passport and \
            "hcl" in passport and \
            "ecl" in passport and \
            "pid" in passport:
        # print("yey")
        counter += 1
    # fields = passport.replace(' ', '\n').split('\n')
    # for field in fields:
    #     print(field)

print(counter)