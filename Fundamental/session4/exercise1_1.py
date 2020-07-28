your_name = input('Your full name: ')
words_list = your_name.split(' ')       
print('Updated:', end = ' ')
for i in words_list:
    if i == '':
        print('', end='')
    else:
        characters = list(i)
        name = str()
        for j in range(len(characters)):
            if j == 0:
                characters[j] = characters[j].upper()
            else:
                characters[j] = characters[j].lower()
            name = name + characters[j]
        print(name, end=' ')