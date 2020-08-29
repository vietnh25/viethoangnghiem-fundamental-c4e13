from pymongo import MongoClient
client = MongoClient()
db = client.get_database('mongo_ex')
mongo_practice = db.get_collection('movies')
post_collection = db.get_collection('posts')
user_collection = db.get_collection('users')
comment_collection = db.get_collection('comments')
# mongo_practice.find()
# data = [
#   {
#   'username' : 'GoodGuyGreg',
#   'comment' : 'Hope you got a good deal!',
#   'post' : post_collection.find_one({'title': 'Borrows something'})['_id']
#   },
#   {
#   'username' : 'GoodGuyGreg',
#   'comment' : "What's mine is yours!",
#   'post' : post_collection.find_one({'title': 'Borrows everything'})['_id']
#   },
#   {
#   'username' : 'GoodGuyGreg',
#   'comment' : "Don't violate the licensing agreement!",
#   'post' : post_collection.find_one({'title': 'Forks your repo on github'})['_id']
#   },
#   {
#   'username' : 'ScumbagSteve',
#   'comment' : "It still isn't clean",
#   'post' : post_collection.find_one({'title': 'Passes out at party'})['_id']
#   },
#   {
#   'username' : 'ScumbagSteve',
#   'comment' : 'Denied your PR cause I found a hack',
#   'post' : post_collection.find_one({'title': 'Reports a bug in your code'})['_id']
#   },

# ]
# comment_collection.insert_many(data)
# mongo_practice.insert_many(data)

# posts = post_collection.aggregate([
#   {
#     '$match': {
#       'username': 'GoodGuyGreg'
#     }
#   },
#   {
#     '$lookup': {
#       'from': 'users',
#       'localField': 'username',
#       'foreignField': 'username',
#       'as': 'user'
#     }
#   }
# ])
# for post in posts:
#   print(post)
  
# x = mongo_practice.find_one()
# for x in mongo_practice.find({'actors' : 'Brad Pitt'}):
#   print(x)

# x = mongo_practice.find_one()
# for x in mongo_practice.find({'franchise' : 'The Hobbit'}):
#   print(x)

# query = {
#   '$or': [{'year':{'$lt': 2000}}, {'year':{'$gte': 2011}}]
# }
# year_query = mongo_practice.find(query)
# for x in year_query:
#   print(x)

# query1 = { 'writer': 'Quentin Tarantino'}
# doc = mongo_practice.find(query1)
# for x in doc:
#   print(x)

# x = mongo_practice.findone()
# x = mongo_practice.find({'sypnosys': {'$regex' : '.*Biblo.*'}})
# for movie in x:
#   print(movie)

