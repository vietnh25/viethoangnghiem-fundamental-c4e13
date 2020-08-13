from pymongo import MongoClient
import pymysql
mongo_connection = MongoClient()
mongo_database = mongo_connection.get_database('cakes')
mongo_collection = mongo_database.get_collection('cakes')

# Connect to the database
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    cursorclass = pymysql.cursors.DictCursor
)

database = connection.cursor()
# database.execute('''
#   CREATE TABLE cakes.cake_filling(
#     cake_id VARCHAR(255),
#     filling_id INT,
#     PRIMARY KEY(cake_id)
#   )
# ''')
# database.execute('''
#     CREATE TABLE cakes.batters(
#         batters VARCHAR(255),
#         PRIMARY KEY(batters)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.topping(
#         topping VARCHAR(255),
#         PRIMARY KEY(topping)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.filling(
#         filling VARCHAR(255),
#         PRIMARY KEY(filling)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.cakes_batters(
#         cakes_id VARCHAR(255),
#         batter_name VARCHAR(255),
#         PRIMARY KEY(cakes_id,batter_name)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.cakes_topping(
#         cakes_id VARCHAR(255),
#         topping_name VARCHAR(255),
#         PRIMARY KEY(cakes_id,topping_name)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.cakes_filling(
#         cakes_id VARCHAR(255),
#         filling_name VARCHAR(255),
#         PRIMARY KEY(cakes_id,filling_name)
#     )
# ''')

# Cakes table
# query = {
#     '_id': {'$ne':None},
#     'type': {'$ne':None},
#     'name': {'$ne':None},
#     'ppu': {'$ne':None}
# }

# cakes_database = mongo_collection.find(query)
# # extract - Read(mongo)
# for cake in cakes_database:
# # Transform
#     cake_id = str(cake['_id'])
#     #Load
#     database.execute(f'''
#         INSERT INTO `cakes`.cake(`_id`,`type`,`name`,`ppu`)
#         VALUES ("{cake_id}","{cake['type']}","{cake['name']}","{cake['ppu']}")
#     ''')
# Batters table
query = [
  {
    '$unwind':'$batters'
  },
  {
    '$group':{
      '_id':'$batters'
    }
  }
]

batters_database = mongo_collection.aggregate(query)

for batters in batters_database:
    database.execute(f'''
        INSERT INTO `cakes`.batters(`name`)
        VALUES("{batters['_id']}")
    ''')


# Cakes_batters table
query = [
  {
    '$unwind':'$batters'
  }
]

cakes_batters_database = mongo_collection.aggregate(query)

for cakes_batters in cakes_batters_database:
    cakes_batters_id = str(cakes_batters["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cakes_batters(`cakes_id`,`batters_name`)
        VALUES("{cakes_batters_id}","{cakes_batters['batters']}")
    ''')

# Topping table
query = [
  {
    '$unwind':'$topping'
  },
  {
    '$group':{
      '_id':'$topping'
    }
  }
]

topping_database = mongo_collection.aggregate(query)

for topping in topping_database:
    database.execute(f'''
        INSERT INTO `cakes`.topping(`name`)
        VALUES("{topping['_id']}")
    ''')

# Cakes_topping table
query = [
  {
    '$unwind':'$topping'
  }
]

cakes_topping_database = mongo_collection.aggregate(query)

for cakes_topping in cakes_toppings_database:
    cakes_topping_id = str(cakes_topping["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cakes_topping(`cakes_id`,`topping_name`)
        VALUES("{cakes_topping_id}","{cakes_topping['topping']}")
    ''')

# Fillings table
query = [
  {
    '$unwind':'$fillings'
  },
  {
    '$group':{
      '_id':'$fillings'
    }
  }
]

fillings_database = mongo_collection.aggregate(query)

for fillings in fillings_database:
    database.execute(f'''
        INSERT INTO `cakes`.fillings(`name`)
        VALUES("{fillings['_id']}")
    ''')

# Cakes_fillings table
query = [
  {
    '$unwind':'$fillings'
  }
]

cakes_fillings_database = mongo_collection.aggregate(query)

for Cakes_fillings in cakes_fillings_database:
    cakes_fillings_id = str(cakes_fillings["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cakes_fillings(`cakes_id`,`fliings_name`)
        VALUES("{cakes_fillings_id}","{cakes_fillings['fillings']}")
    ''')
        
connection.commit()    