number_1_0 = int(input('Enter total of 1 and 0: '))
for i in range(number_1_0):
    if i % 2 == 0:
        print('0', end=' ')
    else:
        print('1', end=' ')    