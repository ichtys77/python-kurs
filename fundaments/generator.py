def number_generator(end):
  n = 1
  while n < end:
    yield n
    n += 1

values = number_generator(10)

print(next(values))
print('Cos tam, cos tam')

for v in values:
  print(v)