def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Ogólny błąd!')
    return a // b

try:
    r = divide(4, 0)
    print(r)
except ZeroDivisionError:
    print('Nie dziel przez 0!')