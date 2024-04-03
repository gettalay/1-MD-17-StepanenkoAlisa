def f(a):
    dictionary = {'Россия': 'Москва', 'Беларусь': 'Минск', 'Германия': 'Берлин', 'Латвия': 'Рига', }
    print(dictionary)
    if a in dictionary:
        b = dictionary[a]
        return b
    else:
        return 'Такой страны не найдено'


a = str(input())
print(f(a))
