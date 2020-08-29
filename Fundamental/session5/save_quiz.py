import pyexcel
from pymongo import MongoClient
mongo_connection = MongoClient()
quiz_database = mongo_connection.get_database('quiz')
quiz_collection = quiz_database.get_collection('quizzes')
records = pyexcel.iget_records(file_name='quizzes.xlsx')
list_data = []
for record in records:
    record['choices'] = record['choices'].split(',')
    list_data.append(record)
# quiz_collection.insert_many(records)
quiz_collection.insert_many(list_data)
for record in records:
    quiz_collection.insert_one({
        'question': record['question'],
        'choices' : record['choices'].split(','),
        'right_choice' : record['right_choice']
    })
