# stuff1 = 'ao tam'
# stuff2 = 'ao mua'
# stuff3 = 'ao phao'

stuffs = ['ao tam','ao mua', 'ao phao','quan boi']

# read one item
# print(stuffs[-1]) 
# ao_mua = stuffs[1]

# Read all 1
# for i in range(len(stuffs)):
#     print(stuffs[i])

# Update
# index = int(input('vi tri muon sua: '))
# new_item = input('ten item moi: ')
# stuffs.append(new_item)
# stuffs[3] = 'quan lanh'

# Create
# new_item = input('enter new item: ')
# stuffs.append(new_item)
# print(len(stuffs))
# Read all 2

# Delete
#stuffs.pop(0) # Delete by index
stuffs.remove('ao tam') # Delete by value

for item in stuffs:
    print(item)    
