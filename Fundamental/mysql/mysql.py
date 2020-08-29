import pymysql

client = pymysql.connect(
  host="localhost",
  user='root',
  password="ngochoang123",
  cursorclass = pymysql.cursors.DictCursor
)

database = client.cursor()

# database.execute("CREATE DATABASE d4e14")

# database.execute('''
#   CREATE TABLE d4e14.center(
#     id VARCHAR(255),
#     name VARCHAR(255),
#     PRIMARY KEY (id)
#   )
# ''')

# database.execute('''
#   CREATE TABLE d4e14.salesman(
#     id VARCHAR(255),
#     name VARCHAR(255),
#     email VARCHAR (255),
#     center_id VARCHAR(255) REFERENCES d4e14.center(id),
#     PRIMARY KEY (id)
#   )
# ''')

# database.execute('''
#   INSERT INTO `d4e14`.center(`id`, `name`)
#   VALUES ('1','22 Thanh Cong'), ('2','91 Chua Lang');
# ''')

salesman = [
  {
    'name':'Duc',
    'email':'123@gmail.com',
    'center_id':1
  },
   {
    'name':'Oanh',
    'email':'1234@gmail.com',
    'center_id':2
  },
  {
    'name':'Truong',
    'email':'3@gmail.com',
    'center_id': 1
  },
  {
    'name':'Ha',
    'email':'356@gmail.com',
    'center_id': 2
  },
]

for i in range(len(salesman)):
  database.execute(f'''
    INSERT INTO `d4e14`.salesman(`id`, `name`, `email`, `center_id`)
    VALUES ("{i}","{salesman[i]['name']}","{salesman[i]['email']}","{salesman[i]['center_id']}");
  ''')

client.commit()
