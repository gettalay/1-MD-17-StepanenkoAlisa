n = int(input())
if n < 37:
    if n % 2 == 0: print('Верхнее купе')
    else: print('Нижнее купе')
if n >= 37:
    if n % 2 == 0: print('Верхнее боковое')
    else: print('Нижнее боковое')