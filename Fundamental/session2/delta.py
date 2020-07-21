from math import sqrt
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

delta = b**2 - 4*a*c

if delta < 0:
  print('Vô Nghiệm')
elif delta == 0:
  x = -b / (2*a)
  print(f'phương trình có nghiệm kép: {x}')
else:
  x1 = (-b + delta**(1/2)) / (2*a)
  x2 = (-b - sqrt(delta)) / (2*a)
  print(f'phương trinh có 2 nghiệm {x1}, {x2}')

