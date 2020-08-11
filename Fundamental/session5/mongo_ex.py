from pymongo import MongoClient
mongo_connection = MongoClient()
new_database = mongo_connection.get_database('mongo_ex')
movie_collection = new_database.get_collection('movies')
comment_collection = new_database.get_collection('comments')
post_collection = new_database.get_collection('posts')
user_collection = new_database.get_collection('users')
# get all documents
print(movie_collection)

