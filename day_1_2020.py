expenses = {int(x) for x in open("input_day_1.txt")}

print(next(x*y for x in expenses for y in expenses if x+y == 2020))