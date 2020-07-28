def up(x, y):
    x = x - 1
    if x < 0:
        print('you do not move up') 
    else:
        global cells_map, x_p, y_p
        x_p = x
        y_p = y
        cells_map[x][y] = 'P'
        cells_map[x+1][y] = '_'
        for i in range(4):
            for j in range(4):
                print(cells_map[i][j], end=' ')
            print()

def down(x, y):
    x = x + 1
    if x > 3:
        print('you do not move down')
    else:
        global cells_map, x_p, y_p
        x_p = x
        y_p = y
        cells_map[x][y] = 'P'
        cells_map[x-1][y] = '_'
        for i in range(4):
            for j in range(4):
                print(cells_map[i][j], end=' ')
            print()

def right(x, y):
    y = y + 1
    if y > 3:
        print('you do not move right')
    else:
        global cells_map, x_p, y_p
        x_p = x
        y_p = y
        cells_map[x][y] = 'P'
        cells_map[x][y-1] = '_'
        for i in range(4):
            for j in range(4):
                print(cells_map[i][j], end=' ')
            print()

def left(x, y):
    y = y - 1
    if y < 0:
        print('you do not move right')
    else:
        global cells_map, x_p, y_p
        x_p = x
        y_p = y
        cells_map[x][y] = 'P'
        cells_map[x][y+1] = '_'
        for i in range(4):
            for j in range(4):
                print(cells_map[i][j], end=' ')
            print()          

from random import *
cells_map= [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]

x_e = randint(0, 3)
y_e = randint(0, 3)
while x_e in range(1, 3) and y_e in range(1, 3):
    x_e = randint(0, 3)
    y_e = randint(0, 3)
cells_map[x_e][y_e] = 'E'

x_k = randint(0, 3)
y_k = randint(0, 3)
while cells_map[x_k][y_k] == cells_map[x_e][y_e]:
    x_k = randint(0, 3)
    y_k = randint(0, 3)
cells_map[x_k][y_k] = 'K'

x_p = randint(0, 3)
y_p = randint(0, 3)
while cells_map[x_p][y_p] == cells_map[x_e][y_e] or cells_map[x_p][y_p] == cells_map[x_k][y_k]:
    x_p = randint(0, 3)
    y_p = randint(0, 3)
cells_map[x_p][y_p] = 'P'

for i in range(4):
    for j in range(4):
        print(cells_map[i][j], end=' ')
    print()
next_count = 0    
while cells_map[x_e][y_e] != 'P':
    move = input('Your move? ')
    if move.upper() == 'W':
        up(x_p, y_p)
        next_count = next_count + 1
    elif move.upper() == 'A':
        left(x_p, y_p)
        next_count = next_count + 1
    elif move.upper() == 'S':
        down(x_p, y_p)
        next_count = next_count + 1
    elif move.upper() == 'D':
        right(x_p, y_p)
        next_count = next_count + 1
    else:
        print('You enter incorrect button')
    if cells_map[x_k][y_k] == 'K' and next_count >= 2:
        print("You can't exit, please acquire the key(s) first")
    if cells_map[x_p][y_p] == cells_map[x_k][y_k]:
        print("You've just picked up a key!!!")
print("Congrats, you've just escaped the dungeon")