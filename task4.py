import random
n, p = 0, 0
while p != 3:
    a1 = random.randint(1, 10)
    a2 = random.randint(1, 10)
    print(a1, ' + ', a2, '= ... ')
    l = int(input())
    if a1 + a2 == l:
        n += 1
        print('Правильно!')
    else:
        p += 1
        print('Ответ неверный')
print('Игра окончена. Верных ответов: ', n)
