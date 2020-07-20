items = ['Áo tắm']  # initialize

def list_out_item():
    for i in range(len(items)):
        print(f'{i+1}.{items[i]}')

action = input('Welcome to our shop, what do you want? (C R U D):  - enter exit quit ')
action = action.upper()
while True:
    if action == 'C':
        new_item = input('Enter new stuff: ')
        items.append(new_item)
        list_out_item()

    elif action == 'R':
        list_out_item()

    elif action == 'U':
        index = int(input('vi tri muon sua: ')) - 1
        if index < len(items):
            new_item = input('ten item moi: ')
            items.append(new_item)    
            list_out_item() 
        else:
            print('item not in list')        
    elif action == "D":
        remove_value = input('nhap gia tri muon xoa: ')
        if remove_value in items:  # check if item have a value in it
            items.remove(remove_value)  
            list_out_item()    
        else:
            print('item not found')   
    elif action == "Exit":
        break


