class Car:
  def __init__(self, model, brand, vinnumber):
    self.model = model
    self.brand = brand
    self.vinnumber = vinnumber
  
  def printInfo(self):
    print('My model is: ', self.model)
    print('My car brand is: ', self.brand)
    print('My car VIN number is: ', self.vinnumber)

myCar1 = Car('Fiesta', 'Ford', '1234567890')
myCar2 = Car('RAV4', 'Toyota', '0987654321')

print('')
myCar1.printInfo()
print('')
myCar2.printInfo()