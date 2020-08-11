from pymongo import MongoClient
from bson import ObjectId
connection = MongoClient()  # connect to mongodb
new_database = connection.get_database('D4E14')
quiz_database = connection.get_database('quiz')  # create / get database
new_collection = new_database.get_collection('students')
result_collection = quiz_database.get_collection('result')
quiz_collection = quiz_database.get_collection('quizzes')
result_found = result_collection.find({'name':'Đức'})
# result_found = result_collection.find({'correct_percent':{'$gt': 0}})
# result_found = result_collection.find({'correct_percent':{'$lt': 0}})
# result_found = result_collection.find({'name':{'$ne': 'Đức'}})
print(list(result_found))

result_collection.update_one(
    {'_id': ObjectId("5f2027920434f3d8dab39bd7")}, # query
    {
        '$unset': {'correct':""}
    } #update
)
result_collection.delete_many(
    {'correct_percent':{'$lte': 50}} #delete
)
quiz_collection.update_one(
    {'_id': ObjectId("5f202ac181d68aa477d30a4f")}, # query
    {
        '$push': {'choices':"7"}
    } #update
)