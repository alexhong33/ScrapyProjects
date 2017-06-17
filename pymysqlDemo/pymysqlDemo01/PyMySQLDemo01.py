'''
Created on 2017年6月16日

@author: Alex

'''

import pymysql.cursors

# Connect to the databse

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='myfirstpydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new table
        sql ='''CREATE TABLE user (
                
                id int(11) NOT NULL AUTO_INCREMENT,
                email varchar(255) COLLATE utf8_bin NOT NULL,
                password varchar(255) COLLATE utf8_bin NOT NULL,
                PRIMARY KEY(id)
        
        
        '''
finally:
    cursor.close()

