inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
            }
print(inventory)
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50
print(inventory)