def shopping(section=[]):
  goods = len(section)
  basket = []
  watching_goods = 0
  while watching_goods < goods:
    print('\nYou take it in your hand: {}'.format(section[watching_goods]))
    decision = input('Do you want to put this product in the basket: ')
    if decision == 'YES':
        basket.append(section[watching_goods])
        section[watching_goods] = ''
    watching_goods += 1
  return basket

def cash_registry(*argv):
  if argv is not None:
    for iarg in argv:
      for good in iarg:   
        print(good, end=', ')
  print('')

shop_shelf1 = ['Apple', 'Orange', 'Banana', 'Kiwi', 'Pear', 'Toy Car']
shop_shelf2 = ['Cookies', 'Chocolate', 'Icecream', 'Goods']

basket1 = shopping(shop_shelf1)
basket2 = shopping(shop_shelf2)

cash_registry(basket1, basket2)