import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'mydb2'
)



mycursor = mydb.cursor()

myquery = 'INSERT INTO students (name,age) VALUES(%s,%s)'

student_info = [('Ravi',12),("Ram",23)]

mycursor.executemany(myquery, student_info)
mydb.commit()

# mycursor.execute('SETECT * FROM students')
# myresult = mycursor.fetchall()
# for var in myresult:
#     print(var)




