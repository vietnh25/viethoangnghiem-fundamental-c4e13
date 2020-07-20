from math import sqrt
a = input('a: ')
b = input('b: ')
c = input('c: ')

delta = b**2 - 4*a*c

if delta < 0:
    print('vo nghiem')
elif delta == 0:
    x = -b / (2*a)
    print(f'phuong trinh co nghiem kep: {x}')    
else:
    x1 = (-b + sqrt(delta)) / (2**a)
    print(f'phuong trinh co 2 nghiem {x1}')

