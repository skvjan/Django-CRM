# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

# issue: Authentication plugin 'caching_sha2_password' is not supported 
# solution: https://www.askpython.com/python/examples/fix-caching_sha2_password-is-not-supported 
# "mysql-connector" does not require after used to above solution

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123',
)

# prepar a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")


#super user
#u: admin
#p: admin123