import math

def main():
    f = open("input.txt", "r")
    max_val=0
    parsed_seats = []
    for ticket in f.readlines():
        parse_row,parse_col = ticket[:7],ticket[7:]
        row = calc_seat(parse_row,0,127,['F','B'])
        col = calc_seat(parse_col,0,7,['L','R'])
        id = (row*8)+col
        parsed_seats.append((id,(row,col)))
    # part 2
    seat = calc_user_seat(parsed_seats)
    print(seat)
    # Part 1
    if id>max_val:
        max_val =id
    return max_val

def calc_user_seat(seats):
    seats.sort(key=lambda x: x[0])
    list_seats = [i for i in range(6,816)]
    user_seat = None
    for i,j in zip(seats,list_seats):
        if i[0] !=j:
            return i[0]
    # return user_seat

def calc_seat(ticket,beg,end,parsable_val):
    row=0
    for i in range(len(ticket)-1):
        if ticket[i] == parsable_val[0]:
            end = math.floor((end+beg)/2)
        elif ticket[i] == parsable_val[1]:
            beg = math.ceil((end+beg)/2)
    return beg if ticket[len(ticket)-1] ==parsable_val[0] else end


print(main())