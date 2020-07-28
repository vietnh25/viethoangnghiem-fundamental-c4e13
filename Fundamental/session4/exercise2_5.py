prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
         }
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
        }
for key in prices:
    print(f'*{key.upper()}')
    print('*price:', prices[key])
    print('*stock:',stock[key])
    print('\n')
total = 0
for key in prices:
    print(f'*{key.upper()}')
    print(f'*If you sold the {key.upper()}, you would make: {prices[key]*stock[key]}')
    print('\n')
    total = total + prices[key]*stock[key]
print(f'*If you sold all of your food, you would make: {total}')