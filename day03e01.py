input = open("share/d03e01-input")

# array = [list(line.strip()) for line in f]
boards = [list(line.strip()) for line in input]
# print(boards[0][1])

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