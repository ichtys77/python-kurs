def gather_info():
  height = float(input('Ile masz wzrostu (metrach)? '))
  weight = float(input('Ile ważysz (w kilogramach)? '))
  return (height, weight)

def calculate_bmi(height, weight):
  bmi = (weight / height)
  return bmi

height, weight = gather_info()
bmi = calculate_bmi(weight, height)
print('Your bmi is: {bmi}')
