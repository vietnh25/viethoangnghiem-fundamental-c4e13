height = 1.80 # meters
weight = 80 # kilograms

print(f"Height: {height} meters")
print(f"Weight: {weight} kilograms")
print()

bmi = round( weight / (height * height), 3)

print(f"BMI = {bmi} ", end='')
if bmi < 25:
    print('Normal.')
elif bmi <= 29:
    print('Overweight.')
else:
    print('Obese!')