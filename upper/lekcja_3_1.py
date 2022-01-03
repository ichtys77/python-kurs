#!/usr/bin/python3

# Zmienne

one_line_string = 'To jest string w jednej linii.'

multi_line_string = '''
To jest string ktory
jest w wiecej
niz jednej lini
to może jeszcze jedna

moze zawierac spacje
        takze wciecia za pomoca tabulacji
  lub spacji
'''
user = 'PiotrKoska'

# print('%s' % (one_line_string))
# print('%s' % (multi_line_string))

# print('-------------------------')

# print('{} to pierwsza zmienna. {} tu druga zmienna'.format(one_line_string, multi_line_string))

# print(f'{one_line_string} to pierwsza zmienna. {multi_line_string} tu druga zmienna')

pozycja_litery = multi_line_string.find('a')

# print('Pozycja {}'.format(pozycja_litery))

# print('72 Pozycja to: {}'.format(multi_line_string[72]))
# print('{} - test dla zmiennej'.format(pozycja_litery))

#print('Zmienna multi_line_string jest: {}'.format(type(multi_line_string)))

# print('zmienna multi_line string to: {}'.format(type(multi_line_string)))

# print('Nazwa Uzytkownika w systemie Linux: {} '.format(user.lower()))
# print('zmniejszam litery w loginie: {}'.format(user.lower()))

print('Rozdzielone\tTabem')
print('To pierwsza linia\nTo druga linia')
