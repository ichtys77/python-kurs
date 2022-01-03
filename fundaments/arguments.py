# def fn(a, b=0, c=0):
#   print('a:', a, 'b:', b, 'c:', c)
#   print(a + b + c)

# fn(2, c=5)

def fn(a, *args, **dict_args):
  print(a)
  for arg in args:
    print(arg)
  for element in dict_args:
    print(element)
    # print(dict_args[element])

fn(3, 2, True, 'sx', 4, 7, user='admin', login=True, db='mongodb')