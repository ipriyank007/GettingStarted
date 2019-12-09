import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="password123",
    database="School"    #Add database after creating.
)

my_cursor = mydb.cursor()

#To create a database:
my_cursor.execute('CREATE DATABASE IF NOT EXISTS School')

#To create table in out Database:
my_cursor.execute('CREATE TABLE IF NOT EXISTS Students (Name VARCHAR(50), Age INTEGER(3))')

#To populate our table:
add_query = 'INSERT INTO Students VALUES(%s, %s)'

#one data
# data = ('john', 22)
# my_cursor.execute(add_query, data)

# multiple data
data_list = [('Neha', 22), ('Samuel', 25), ('Robert', 27)]
my_cursor.executemany(add_query, data_list)

mydb.commit()

