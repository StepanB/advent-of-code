input = open("share/d03e01-input")

boards = [list(line.strip()) for line in input]

right_shift = 1
down_shift = 1
x = 0
y = 0
counter = 0
multy = 1;

while y < len(boards):

    if x > len(boards[y]) - 1:
        x -= len(boards[y])

    if boards[y][x] == '#':
        counter += 1

    x += right_shift
    y += down_shift

print(counter) # 247
multy *= counter

right_shift = 3
down_shift = 1
x = 0
y = 0
counter = 0

while y < len(boards):

    if x > len(boards[y]) - 1:
        x -= len(boards[y])

    if boards[y][x] == '#':
        counter += 1

    x += right_shift
    y += down_shift

print(counter) # 247
multy *= counter

right_shift = 5
down_shift = 1
x = 0
y = 0
counter = 0

while y < len(boards):

    if x > len(boards[y]) - 1:
        x -= len(boards[y])

    if boards[y][x] == '#':
        counter += 1

    x += right_shift
    y += down_shift

print(counter) # 247
multy *= counter

right_shift = 7
down_shift = 1
x = 0
y = 0
counter = 0

while y < len(boards):

    if x > len(boards[y]) - 1:
        x -= len(boards[y])

    if boards[y][x] == '#':
        counter += 1

    x += right_shift
    y += down_shift

print(counter) # 247
multy *= counter

right_shift = 1
down_shift = 2
x = 0
y = 0
counter = 0

while y < len(boards):

    if x > len(boards[y]) - 1:
        x -= len(boards[y])

    if boards[y][x] == '#':
        counter += 1

    x += right_shift
    y += down_shift

print(counter) # 247
multy *= counter
print(multy)