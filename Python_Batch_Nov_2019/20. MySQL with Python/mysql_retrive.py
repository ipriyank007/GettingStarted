import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="School"
)

curr = mydb.cursor()

#all rows and column of the database
# curr.execute('SELECT * FROM Students')

#Get all column for selective rows:
#curr.execute('SELECT * FROM Students WHERE Age<24')

#Get specific column:
#curr.execute('SELECT Name FROM Students')

# Get Specific columns and rows
# curr.execute('SELECT Name FROM Students WHERE Age > 24')

# Wildcard in mysql
# curr.execute('SELECT * FROM Students WHERE Name LIKE "%a%"')

for row in curr:
    print(row)