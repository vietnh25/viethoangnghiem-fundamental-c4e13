n = int(input('Enter the number of months: '))
for i in range(n+1):
    if i == 0:
        month_0 = 1
        print(f'Month {i}: {month_0} pair of rabbit')
    elif i == 1:
        month_1 = 2
        print(f'Month {i}: {month_1} pairs of rabbit')
    else:
        if i%2 == 0:
            month_0 = month_0 + month_1
            print(f'Month {i}: {month_0} pairs of rabbit')
        else:
            month_1 = month_1 + month_0
            print(f'Month {i}: {month_1} pairs of rabbit')