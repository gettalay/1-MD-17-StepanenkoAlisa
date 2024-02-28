s = ''
while s != 'stop':
    s = str(input())
    if s == 'stop':
        break
    if 'ф' in s or 'Ф' in s:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')
