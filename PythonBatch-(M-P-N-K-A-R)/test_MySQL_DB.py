import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'host',
    passwd = 'password',
    database = 'pythontest'
)

mycursor = mydb.cursor()

# sqlquery = ' INSERT INTO students (name, age) VALUES (%s, %s)'
#
# student = [('Rahul',15),('Drake', 16), ('Payal',15)]
mycursor.execute('SELECT name FROM students WHERE age = 17')
result = mycursor.fetchall()

for i in result:
    print(i)
# mycursor.executemany(sqlquery,student)

# mydb.commit()






















# mycursor = mydb.cursor()
#
# myquery = 'INSERT INTO students (name,age) VALUES(%s,%s)'
#
# student_info = [('Ravi',12),("Ram",23)]
#
# mycursor.executemany(myquery, student_info)
# mydb.commit()

# mycursor.execute('SETECT * FROM students')
# myresult = mycursor.fetchall()
# for var in myresult:
#     print(var)




