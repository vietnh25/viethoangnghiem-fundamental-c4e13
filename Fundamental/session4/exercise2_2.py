numbers = [1, 6, 8, 1, 2, 1, 5, 6]
number = int(input('Enter a number? '))
appear_count = 0
for i in numbers:
    if i == number:
        appear_count = appear_count + 1
if appear_count == 0:
    print(f'{number} does not appear in my list')
elif appear_count == 1:
    print(f'{number} appears {appear_count} time in my list')
else:
    print(f'{number} appears {appear_count} times in my list')