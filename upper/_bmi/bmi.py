def gather_info():
  height = float(input('Ile masz wzrostu (metrach)? '))
  weight = float(input('Ile ważysz (w kilogramach)? '))
  return (height, weight)

def calculate_bmi(height, weight):
  bmi = (weight / (height ** 2))
  return bmi

height, weight = gather_info()
bmi = calculate_bmi(height, weight)
print(f'Your bmi is: {bmi}')