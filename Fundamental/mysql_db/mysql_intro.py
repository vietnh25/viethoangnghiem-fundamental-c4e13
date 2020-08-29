import pymysql
# Connect to the database
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    cursorclass = pymysql.cursors.DictCursor
)
cursor = connection.cursor()
# cursor.execute('''
    #     CREATE TABLE d4e14.center(
    #         id VARCHAR(255),
    #         name VARCHAR(255),
    #         PRIMARY KEY (id)
    #     )
    # '''
    # cursor.execute('''
    #     CREATE TABLE d4e14.saleman(
    #         id VARCHAR(255),
    #         name VARCHAR(255),
    #         email VARCHAR(255),
    #         center_id VARCHAR(255) REFERENCES d4e14.center(id),
    #         PRIMARY KEY (id)
    #     )
    # ''') 
# cursor.execute('''
#         INSERT INTO `d4e14`.center(`id`,`name`) VALUES 
#         ('1','22 Thành Công'),
#         ('2','91 Chùa Láng');
#      ''')

salesman = [
    {
        'name':'Oanh',
        'email':'123@gmail.com',
        'center_id':1
    },
    {
        'name':'Đức',
        'email':'1234@gmail.com',
        'center_id':2
    },
    {
        'name':'Trường',
        'email':'5@gmail.com',
        'center_id':1
    },
    {
        'name':'Hà',
        'email':'456@gmail.com',
        'center_id':2
    }
]
for i in range(len(salesman)):
    # print(salesman[i]['name'])
    cursor.execute(f'''
INSERT INTO `d4e14`.saleman(`id`,`name`,`email`,`center_id`) VALUES
("{i}","{salesman[i]['name']}","{salesman[i]['email']}","{salesman[i]['center_id']}");
    ''')

# connection is not autocommit by default. So you must commit to save
# your changes.
connection.commit()     
 