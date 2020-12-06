input = open("share/d02e01-input", "r")
counter = 0

for line in input:
    # Nacist radek
    print(line.strip())

    # Rozdelit radek na potrebne hodnoty
    data = line.strip().split()
    print(data)

    # Zjistit kolikrat je pismeno v posledni casti
    count = data[2].count(data[1][0])
    print(count)

    # Zjistit jestli je pocet vyskytu pismene v rozsahu:
    min_max = data[0].split("-")
    # print(min_max)
    if(count >= int(min_max[0]) and count <= int(min_max[1])):
        counter += 1


print(counter) # 454