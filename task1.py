#remember about single file
def f(a):
    if a % 7 == 0:
        return 'Число делится'
    else: return 'Число не делится'
b = int(input())
print(f(b))