

import pymysql 

def connect():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='estoque',
        port=3308,
        autocommit=True 
    )

# connection = connect() 

# connection.close()