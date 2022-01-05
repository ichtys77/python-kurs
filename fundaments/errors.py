try:
    print('Dzielenie wyjdzie?')
    a = 2 / 0
    print(a)
except ZeroDivisionError:
    print('Error! - dzielenie przez 0')