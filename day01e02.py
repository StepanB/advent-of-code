input = open('share/d01e01-input', 'r')
list_input = list(range(0))

for line in input:
    list_input.append(line.strip())

i = 0;
print(i)
for num in list_input:
    for another_num in list_input:
        # print(num + " + " + another_num + " = " + num+another_num)
        for just_another_num in list_input:

            i += 1;
                # break;

print("i = {}".format(i))

j = 0
for x in range(0, len(list_input)):
    for y in range(x, len(list_input)):
        for z in range(y, len(list_input)):
            if int(list_input[x]) + int(list_input[y]) + int(list_input[z]) == 2020:
            # if int(num) + int(another_num) +int(just_another_num) == 2020:
                print(int(list_input[x]) * int(list_input[y]) * int(list_input[z]));

            j += 1

print("j = {}".format(j))
print(list_input)