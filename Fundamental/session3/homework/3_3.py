# chưa tối ưu 
flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is X and these are my sheep sizes', flock)
print()
grown1 = []
for grow in flock:
    grow = grow + 50
    grown1.append(grow)
print('One month after, here is my flock', grown1)

shear_bigg = max(grown1)
print('Now my biggest sheep has its size of', shear_bigg, "let's shear it")
b = grown1.index(shear_bigg)
grown1.pop(b)
grown1.insert(b, 8)
print('After shearing, here is my flock', grown1)
print()

grown2 = []
for grow in grown1:
    grow = grow + 50
    grown2.append(grow)
print('One month after, here is my flock', grown2)

shear_big = max(grown2)
print('Now my biggest sheep has its size of', shear_big, "let's shear it")

c = grown2.index(shear_big)
grown2.pop(c)
grown2.insert(c, 8)
print('After shearing, here is my flock', grown2)
print()

grown3 = []
for grow in grown2:
    grow = grow + 50
    grown3.append(grow)
print('One month after, here is my flock', grown3)

size = sum(grown3)
print('My flock has size in total:', size)
worth = 2 * size
print('I would get', size, '* 2$ =', worth, '$')