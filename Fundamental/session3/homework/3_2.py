import random
word = ['meticulous', 'champion', 'hexagon']
picked = random.choice(word)
listed = list(picked)
random.shuffle(listed)
for i in listed:
    print('', i, end='')
print()
ans = input('Enter your answer?')
if ans == picked:
    print('Correct ^^:', picked)
else:
    print('Wrong!')