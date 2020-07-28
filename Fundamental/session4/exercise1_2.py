balance = float(input('Enter your balance: '))
balance_parts = str(balance).split('.')
standardise_balance = str()
balance_part_1 = list(balance_parts[0])
for i in range(-len(balance_part_1) + 1, 0):       
    if i%3 == 0:
        balance_part_1.insert(i, ',')
for i in range(len(balance_part_1)):
        standardise_balance = standardise_balance + balance_part_1[i]
if balance_parts[1] != '0':
    standardise_balance = standardise_balance + '.' + balance_parts[1]
print('Your updated balance: ','$'+standardise_balance)