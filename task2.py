def f(a):
    if type(a) != int:
        return 'ValueError'
    else:
        if a == 0:
            return 'ZeroDivisionError'
        else:
            if 200 % int(a) == 0:
                return 'Число делится'
            else:
                return 'Число не делится'
b = input()
print(f(b))