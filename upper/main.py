from class_Car import Car

value = float(input('Podaj ile w baku: '))
unit = input('L dla litrów, G dla galonów: ')

myCar = Car()
myCar.setTank(value, unit)

while True:
  choice = int(input('0 - przelicz, 1 - liczba litrów w baku, 2 - wyjście: '))
  if choice == 2:
    break
  elif choice == 0:
    unit = (input('L dla litrów, G dla galonów: '))
    print(myCar.getTank(unit)) 
  elif choice == 1:
    value = float(input('Podaj ile w baku: '))
    unit = (input('L dla litrów, G dla galonów: '))
    myCar.setTank(value)
  else:
    pass
