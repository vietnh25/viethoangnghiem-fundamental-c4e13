from pymongo import MongoClient
client = MongoClient()
db = client.get_database('mongo_ex')
movies = db.get_collection('movies')
# Q1. 
# movies.find({})
# Q2. 
movies.find({'writer:' "Quentin Tarantino"})
# Q3. 
# movies.find({"actors": "Brad Pitt"})
# Q4. 
# movies.find({'franchise:' "The Hobbit"})
# Q5. 
# movies.find({'year:' {'$gte': 1990, '$lte': 1999}})
# Q6. 
# movies.find({'$or':[{'year':{'$lte':2000}}, {'year':{'$gte':2010}}]})

# U1. 
# movies.update_one({'title': "The Hobbit: An Unexpected Journey"}, {'$set': {'synopsis': "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}})
# U2. 
# movies.update_one({'title': "The Hobbit: The Desolation of Smaug"}, {'$set': {'synopsis': "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."}})
# U3: 
# movies.update_one({'title': "Pulp Fiction"}, {'$push': {'actors': "Samuel L. Jackson"}})

# TS1:.
# movies.find({'synopsis': {'$regex': '.*Bilbo'}})
# TS2:.
# movies.find({'synopsis': {'$regex':'.*Gandalf.*'}})
# TS3:.
# movies.find({'$and': [{'synopsis': {'$regex': '.*Bilbo'}}, {'synopsis': {'$regex':'.*Gandalf.*'}} ]})
# TS4:.
# movies.find({'$and': [{'synopsis': {'$regex':'.*Gandalf.*'}}, {'$not': {'synopsis': {'$regex':'.*Gandalf.*'}}}]})
# TS5:.
# movies.find({'$or': [{'synopsis': {'$regex':'.*dwarves.*'}}, {'synopsis': {'$regex': '.*hobbit.*'}}]})

# D1: 
# movies.delete_one({'title': "Pee Wee Herman's Big Adventure"})
# D2: 
# movies.delete_one({'title': "Avatar"})

# R1: 
# users.find({})
# R2: 
# posts.find({})
# R3: 
# posts.find({'username': "GoodGuyGreg"})
# R4: 
# posts.find({'username': "ScumbagSteve"})
# R5: 
# comments.find({})
# R6: 
# comments.find({'username': "GoodGuyGreg"})
# R7: 
# comments.find({'username': "ScumbagSteve"})
# R8: 
# comments.find({'post': posts.find_one({'title': "Reports a bug in your code"})['_id']})