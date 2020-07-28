from random import *
def summation(a, b):
    c = choice([-10, -1, 0, 0, 0, 0, 1, 10])
    print(f'{a} + {b} = {a + b + c}')
    answer = input('Your answer is (Y/N)? ')
    if c == 0:
        if answer.upper() == 'Y':
            print('Your answer is right')
            global correct_answer
            correct_answer = correct_answer + 1
        else:
            print('Your answer is wrong')
            global incorrrect_answer
            incorrrect_answer = incorrrect_answer + 1
    else:
        if answer.upper() == 'Y':
            print(f'Your answer is wrong, {a} + {b} = {a + b}')
            incorrrect_answer = incorrrect_answer + 1
        else:
            print(f'Your answer is right, {a} + {b} = {a + b}')
            correct_answer = correct_answer + 1
    print()

def subtraction(a, b):
    c = choice([-10, -1, 0, 0, 0, 0, 1, 10])
    print(f'{a} - {b} = {a - b + c}')
    answer = input('Your answer is (Y/N)? ')
    if c == 0:
        if answer.upper() == 'Y':
            print('Your answer is right')
            global correct_answer
            correct_answer = correct_answer + 1
        else:
            print('Your answer is wrong')
            global incorrrect_answer
            incorrrect_answer = incorrrect_answer + 1
    else:
        if answer.upper() == 'Y':
            print(f'Your answer is wrong, {a} - {b} = {a - b}')
            incorrrect_answer = incorrrect_answer + 1
        else:
            print(f'Your answer is right, {a} - {b} = {a - b}')
            correct_answer = correct_answer + 1
    print()

def multiplication(a, b):
    c = choice([-100, -10, -1, 0, 0, 0, 0, 0, 0, 1, 10, 100])
    print(f'{a} * {b} = {a * b + c}')
    answer = input('Your answer is (Y/N)? ')
    if c == 0:
        if answer.upper() == 'Y':
            print('Your answer is right')
            global correct_answer
            correct_answer = correct_answer + 1
        else:
            print('Your answer is wrong')
            global incorrrect_answer
            incorrrect_answer = incorrrect_answer + 1
    else:
        if answer.upper() == 'Y':
            print(f'Your answer is wrong, {a} * {b} = {a * b}')
            incorrrect_answer = incorrrect_answer + 1
        else:
            print(f'Your answer is right, {a} * {b} = {a * b}')
            correct_answer = correct_answer + 1
    print()

def math_quizzes(a, b):
    operations = ['summation', 'subtraction', 'multiplication']
    operation = choice(operations)
    if operation == 'summation':
        summation(a, b)
    elif operation == 'subtraction':
        subtraction(a, b)
    elif operation == 'multiplication':
        multiplication(a, b)

incorrrect_answer = 0
correct_answer = 0
for i in range(5):
    math_quizzes(randint(10, 100), randint(10, 100))
print('Your correct number of answers: ', correct_answer)
print('Your incorrect number of answers: ', incorrrect_answer)