input = open("share/d02e01-input", "r")
counter = 0

for line in input:
    # Nacist radek
    print(line.strip())

    # Rozdelit radek na potrebne hodnoty
    data = line.strip().split()
    print(data)

    # Zjistit co
    # count = data[2].count(data[1][0])
    # print(count)
    # letter = dat

    # Zjistit jestli je zadane pismeno na danych pozicich
    position = data[0].split("-")
    position[0] = int(position[0])-1
    position[1] = int(position[1])-1

    if (data[1][0] == data[2][int(position[0])] and data[1][0] != data[2][int(position[1])]) or (data[1][0] != data[2][int(position[0])] and data[1][0] == data[2][int(position[1])]):
        counter += 1


print(counter) # 649
