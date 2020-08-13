import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_database = mongo_client.get_database('cakes_ex')
mongo_collection = mongo_database.get_collection('cakes')

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    cursorclass = pymysql.cursors.DictCursor
)

database = client.cursor()

database.execute("CREATE DATABASE cakes")

database.execute('''
    CREATE TABLE cakes.cakes(
        _id VARCHAR(255),
        type VARCHAR(255),
        name VARCHAR(255),
        ppu DECIMAL(10,2),
        PRIMARY KEY(_id)
    )
''')

database.execute('''
    CREATE TABLE cakes.batters(
        id INT,
        type VARCHAR(255),
        PRIMARY KEY(id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.topping(
        id INT,
        type VARCHAR(255),
        PRIMARY KEY (id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.filling(
        id INT,
        type VARCHAR(255),
        PRIMARY KEY (id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_batter(
        cake_id VARCHAR(255),
        batter_id INT,
        PRIMARY KEY (cake_id, batter_id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_topping(
        cake_id VARCHAR(255),
        topping_id INT,
        PRIMARY KEY (cake_id, topping_id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_filling(
        cake_id VARCHAR(255),
        filling_id INT,
        PRIMARY KEY (cake_id, filling_id)
    )
''')

# Cakes table
query = {
    '_id':{'$ne':None},
    'type':{'$ne':None},
    'name':{'$ne':None},
    'ppu':{'$ne':None},
    'batters':{'$ne':None},
    'filling':{'$ne':None},
    'topping':{'$ne':None}
}

cakes_database = mongo_collection.find(query)

for cakes in cakes_database:
    cakes_id = str(cakes['_id'])
    database.execute(f'''
        INSERT INTO `cakes`.cakes(`id`,`type`,`name`,`ppu`)
        VALUES("{cakes_id}","{cakes['type']}","{cakes['name']}","{cakes['ppu']}")
    ''')

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

for cakes_topping in cakes_topping_database:
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

for cakes_fillings in cakes_fillings_database:
    cakes_fillings_id = str(cakes_fillings["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cakes_fillings(`cakes_id`,`fliings_name`)
        VALUES("{cakes_fillings_id}","{cakes_fillings['fillings']}")
    ''')

client.commit()
