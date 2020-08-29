from pymongo import MongoClient
import pyexcel as pe
connection = MongoClient()  # connect to mongodb

quiz_database = connection.get_database('quiz')  # create / get database

result_collection = quiz_database.get_collection('result')
quizzes_collection = quiz_database.get_collection('quizzes')
quizzes = quizzes_collection.find()
# print(list(quizzes))
right_choice_count = 0

quizzes = list(quizzes)

# quizzes.append
for quiz in quizzes:
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

# data = {
#     'name': 'Đức',
#     'correct_percent' : correct_percent
# }
# result_collection.insert_one(data) # write document to collection
