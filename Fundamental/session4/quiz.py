import pyexcel as pe 
# from turtle import * # tu thu vien turtle 
quizzes = pe.iget_records(file_name="quizzes.xlsx")

# for quiz in quizzes:
#     quiz['choices'] = quiz['choices'].split(',')

# quizzes = [
#     {
#         'question' : 'con nhện có mấy chân',
#         'choices': [3,4,5,6],
#         'right_choice': 3
#     },
#     {
#         'question' : 'con chó có mấy chân',
#         'choices': [3,4,5,6],
#         'right_choice': 1
#     },
#     {
#         'question' : 'con gà có mấy chân',
#         'choices': [3,4,5,2],
#         'right_choice': 3
#     }
# ]    
right_choice_count = 0

quizzes = list(quizzes)
# quizzes.append
for quiz in quizzes:
    quiz['choices'] = quiz['choices'].split(',')
    # in question and choice
    print(quiz['question'])
    for i in range(len(quiz['choices'])):
        print(f' {i+1}.{quiz["choices"][i]}')

    # lua chon dap an
    your_choice = int(input('your choice: ')) - 1
    if your_choice == int(quiz['right_choice']):
        # print('Correct') # dap an dung
        right_choice_count = right_choice_count + 1
    else:
        print('Not Correct')    
correct_percent = right_choice_count / len(quizzes) * 100
print(f'{correct_percent}%')
data = [
    ['Đức', f'{correct_percent}%']
]
pe.save_as(array=data, dest_file_name='quiz.xls')

    
