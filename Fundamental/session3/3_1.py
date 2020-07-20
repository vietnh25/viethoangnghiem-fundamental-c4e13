
stuffs = ['but bi','but chi','but muc']
v = 3
while v <= 3:
    lua_chon = input('welcome to our shop, what do you want? (C R U D):')
    # Read
    if lua_chon == "R":  
        for item in stuffs:
            print(item)  
        print()  
    # Create    
    elif lua_chon == "C":
        new_item = input('enter new item: ')
        stuffs.append(new_item)
        for item in stuffs:
            print(item)  
        print()
    # Update
    elif lua_chon == "U":
        index = int(input('vi tri muon sua: '))
        new_item = input('ten item moi: ')
        stuffs.append(new_item)    
        for item in stuffs:
            print(item) 
        print()
    # Delete
    elif lua_chon == "D":
        index = int(input('vi tri muon xoa: '))
        stuffs.pop(index)  
        for item in stuffs:
            print(item) 
        print()  


