import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_database = mongo_client.get_database('cakes')
mongo_collection = mongo_database.get_collection('cakes')

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    cursorclass = pymysql.cursors.DictCursor
)

database = client.cursor()

# database.execute("CREATE DATABASE cakes")

# database.execute('''
#     CREATE TABLE cakes.cakes(
#         _id VARCHAR(255),
#         type VARCHAR(255),
#         name VARCHAR(255),
#         ppu DECIMAL(10,2),
#         PRIMARY KEY(_id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.batters(
#         id INT,
#         type VARCHAR(255),
#         PRIMARY KEY(id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE `cakes`.topping(
#         id INT,
#         type VARCHAR(255),
#         PRIMARY KEY (id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE `cakes`.filling(
#         id INT,
#         type VARCHAR(255),
#         PRIMARY KEY (id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE `cakes`.cake_batter(
#         cake_id VARCHAR(255),
#         batter_id INT,
#         PRIMARY KEY (cake_id, batter_id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE `cakes`.cake_topping(
#         cake_id VARCHAR(255),
#         topping_id INT,
#         PRIMARY KEY (cake_id, topping_id)
#     )
# ''')

# database.execute('''
#     CREATE TABLE cakes.fillings(
#         id INT,
#         name VARCHAR(255),
#         addcost DECIMAL(10,2),
#         PRIMARY KEY (id, addcost)
#     )
# ''')

# Cakes table
query = {
    'type': {'$ne': None},
    'name': {'$ne': None},
    'ppu': {'$ne': None}
}
cakes = mongo_collection.find(query)
for cake in cakes:
    database.execute(f'''
        INSERT INTO `cakes`.cakes(`_id`, `type`, `name`, `ppu`)
        VALUES("{cake['_id']}", "{cake['type']}", "{cake['name']}", {cake['ppu']})
    ''')


# Batters table
query = [
    {'$unwind': '$batters.batter'},
    {'$group': {'_id': '$batters.batter'}}
]
batters = mongo_collection.aggregate(query)
for batter in batters:
    database.execute(f'''
        INSERT INTO `cakes`.batters(`id`, `type`)
        VALUES({batter['_id']['id']}, "{batter['_id']['type']}")
    ''')

# Cakes_batters table
query = [{'$unwind': '$batters.batter'}]
cake_batter_database = mongo_collection.aggregate(query)
for cake_batter in cake_batter_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_batter(`cake_id`, `batter_id`)
        VALUES("{cake_batter['_id']}", {cake_batter['batters']['batter']['id']})
    ''')

# Topping table
query = [
    {'$unwind': '$topping'},
    {'$group': {'_id': '$topping'}}
]
toppings = mongo_collection.aggregate(query)
for topping in toppings:
    database.execute(f'''
        INSERT INTO `cakes`.topping(`id`, `type`)
        VALUES({topping['_id']['id']}, "{topping['_id']['type']}")
    ''')

# Cakes_topping table
query = [{'$unwind': '$topping'}]
cake_topping_database = mongo_collection.aggregate(query)
for cake_topping in cake_topping_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_topping(`cake_id`, `topping_id`)
        VALUES("{cake_topping['_id']}", {cake_topping['topping']['id']})
    ''')

# Fillings table
query = [
    {'$unwind': '$fillings.filling'},
    {'$group': {'_id': '$fillings.filling'}}
]
fillings = mongo_collection.aggregate(query)
for filling in fillings:
    database.execute(f'''
        INSERT INTO `cakes`.fillings(`id`, `name`, `addcost`)
        VALUES({filling['_id']['id']}, "{filling['_id']['name']}", {filling['_id']['addcost']})
    ''')

# Cakes_fillings table
query = [{'$unwind': '$fillings.filling'}]   
cake_filling_database = mongo_collection.aggregate(query)
for cake_filling in cake_filling_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_filling(`cake_id`, `filling_id`)
        VALUES("{cake_filling['_id']}", {cake_filling['fillings']['filling']['id']})
    ''') 

client.commit()
