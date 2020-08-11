from pymongo import MongoClient
import pymysql
mongo_connection = MongoClient()
mongo_database = mongo_connection.get_database('mongo_ex')
mongo_collection = mongo_database.get_collection('movies')

# Connect to the database
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    cursorclass = pymysql.cursors.DictCursor
)

database = connection.cursor()

# query = {
#     'title': {'$ne':None},
#     'writer': {'$ne':None},
#     'year': {'$ne':None},
#     'actors': {'$ne':None}
# }

# movies_database = mongo_collection.find(query)
# # extract - Read(mongo)
# for movie in movies_database:
# # Transform
#     # print(movie['title'])
#     movie_id = str(movie['_id'])
#     #Load
#     database.execute(f'''
#         INSERT INTO `movies`.movies(`id`,`title`,`writer`,`year`)
#         VALUES ("{movie_id}","{movie['title']}","{movie['writer']}","{movie['year']}")
#     ''')

# query = [
#     {
#         '$unwind' : '$actors'
#     },
#     {
#         '$group' :{
#             '_id':'$actors'
#         }
#     }
# ]
# actors_database = mongo_collection.aggregate(query)
# # extract - Read(mongo)
# for actor in actors_database:
# # Transform
#     #Load
#     database.execute(f'''
#         INSERT INTO `movies`.actor(`name`)
#         VALUES ("{actor['_id']}")
#     ''')
#movie_actor
# database.execute('''
#   CREATE TABLE movies.movie_actor(
#     movies_id VARCHAR(255),
#     actor_name VARCHAR(255),
#     PRIMARY KEY(movies_id, actor_name)
#   )
# ''')
query = [
  {
    '$unwind':'$actors'
  }
]

movie_actor_database = mongo_collection.aggregate(query)

for movie_actor in movie_actor_database:
  movie_actor_id = str(movie_actor["_id"])
  database.execute(f'''
    INSERT INTO `movies`.movie_actor(`movies_id`,`actor_name`)
    VALUES("{movie_actor_id}","{movie_actor['actors']}")
  ''')
connection.commit()


# Create database movies
# database.execute('CREATE DATABASE movies')

#create table movies
# database.execute('''
#         CREATE TABLE movies.movies(
#             id VARCHAR(255),
#             title VARCHAR(255),
#             writer VARCHAR(255),
#             year VARCHAR(255),
#             PRIMARY KEY (id)
#         )
#     ''')

# database.execute('''
#         CREATE TABLE movies.movie_actor(
#             movie_id VARCHAR(255),
#             actor_name VARCHAR(255),
#             PRIMARY KEY (movie_id)
#         )
#     ''')  





