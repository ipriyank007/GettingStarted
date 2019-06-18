import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'myfirstdb'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IF EXISTS myfirstdb")
# mycursor.execute("CREATE TABLE IF EXISTS students (Name VARCHAR(250), Age INTEGER(3))")
# sqlformula = "INSERT INTO students (Name, Age) VALUES (%s, %s)"
# details = ('Priyank', 24)
# details = [('Jack', 115), ('Bucky', 29), ('Sam', 27)]
# mycursor.executemany(sqlformula, details)
# mydb.commit()

# mycursor.execute("SELECT * FROM students")
#
# for row in mycursor:
#     print(row)

# mycursor.execute("SELECT * FROM students WHERE Name LIKE '%ky'")
#
# for row in mycursor:
#     print(row)

# mycursor.execute("UPDATE students SET Age=30 WHERE Name='Bucky'")
# mydb.commit()

# mycursor.execute("SELECT * FROM students LIMIT 2 OFFSET 1")
#
# for row in mycursor:
#     print(row)

# mycursor.execute("SELECT * FROM students ORDER BY Name DESC")
#
# for row in mycursor:
#     print(row)

# mycursor.execute("DELETE FROM students WHERE Name='Sam'")
# mydb.commit()

# mycursor.execute('DROP TABLE IF EXISTS students')
# mydb.commit()

mycursor.execute('DROP DATABASE IF EXISTS myfirstdb')
mydb.commit()