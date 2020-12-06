input = open('share/d01e01-input', 'r')
list_input = list(range(0))

for line in input:
    list_input.append(line.strip())

i = 0
for x in range(0, len(list_input)):
    for y in range(x, len(list_input)):
        # print(i)
        # i += 1
        # print(num + " + " + another_num + " = " + num+another_num)
        if int(list_input[x]) + int(list_input[y]) == 2020:
            print(int(list_input[x]) * int(list_input[y]));
            break;


print(list_input)