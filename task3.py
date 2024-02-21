year = int(input())
if year % 4 != 0: print('Год обычный')
else:
    if year % 100 != 0: print('Год високосный')
    else:
        if year % 400 != 0: print('Год обычный')
if year % 400 == 0 and year % 100 == 0: print('Год високосный')
