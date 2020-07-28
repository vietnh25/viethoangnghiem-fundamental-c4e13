number = int(input('How many B bacterias are there? '))
time = int(input('How much time in minutes will we wait? '))
after_number = number*(2**(time//2))
print(f'After {time} minutes, we would have {after_number} bacterias')