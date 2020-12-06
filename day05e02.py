import math

input = open("share/d05e01-input", "r")
max = 0
min = 1000
seats = [*range(7, 909, 1)]

def get_seat_id(row, column):
    return row * 8 + column


def get_row(param):
    # print(param)
    max = 127
    min = 0
    # middle = math.floor(max/2)
    for x in param:
        # print("range id {} - {}".format(min, max))
        if x == 'F' :
            max = math.floor((max-min) / 2 + min)
        else:
            min = math.ceil((max-min) / 2 + min)
    if param[6] == 'F':
        return min

    return max



def get_column(param):
    # print(param)
    max = 7
    min = 0
    # middle = math.floor(max/2)
    for x in param:
        # print("range id {} - {}".format(min, max))
        if x == 'L' :
            max = math.floor((max-min) / 2 + min)
        else:
            min = math.ceil((max-min) / 2 + min)
    if param[2] == 'L':
        return min

    return max


def get_max(current_max, seat_id):
    if seat_id > current_max:
        return seat_id

    return current_max


def get_min(curr_min, seat_id):
    if seat_id < curr_min:
        return seat_id

    return curr_min


for line in input:
    row = get_row(line[0:7])
    column = get_column(line[7:10])

    # print(row)
    # print(column)
    seat_id = get_seat_id(row, column)
    seats.remove(int(seat_id))
    print(seat_id)
    max = get_max(max, seat_id)
    min = get_min(min, seat_id)




print("\n\nCurrent max {}".format(max))
print("Current min {}".format(min))
print(seats) # 619