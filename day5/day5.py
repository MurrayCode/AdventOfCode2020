import csv
import functools
import operator


with open('input.csv')as f:
    reader = csv.reader(f, delimiter='\n')
    input = list(reader)
    merged = functools.reduce(operator.iconcat, input, [])



def check(data: list):

    idlist = []
    highest_id = 0

    for ticket in data:
        n = 7
        split_strings = [ticket[index : index + n] for index in range(0, len(ticket), n)]
        seat_num=split_strings[0] 
        column_num=split_strings[1]

        top_row_range = 127
        bot_row_range = 0
        top_col_range = 7
        bot_col_range = 0
        final_row_num = 0
        final_col_num = 0
        for letter in seat_num:
            half = (top_row_range + bot_row_range) / 2
            if letter == "F":
                top_row_range = half
                final_row_num = top_row_range
            elif letter == "B":
                bot_row_range = half
                final_row_num = bot_row_range

        for x in column_num:
            half = (top_col_range + bot_col_range) / 2
            if x == "L":
                top_col_range = half
                final_col_num = top_col_range
            elif x == "R":
                bot_col_range = half
                final_col_num = bot_col_range
        y = round(final_row_num, 0)
        x = round(final_col_num, 0)
        seatid = y * 8 + x
        if seatid > highest_id:
            highest_id = seatid
        final = "Row: " + str(y) + " column: " + str(x) + " id: " + str(seatid)
        idlist.append(final)
    return idlist

list = check(merged)
list.sort()
print(list)