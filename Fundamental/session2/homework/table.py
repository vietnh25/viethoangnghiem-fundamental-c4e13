n = int(input('Nhap n: '))

for y in range(1, n):
    for x in range(1, n):
        if x * y >= 10:
            print(x * y, end=' ')
        else:
            print(x * y, end=' ')
    print()        