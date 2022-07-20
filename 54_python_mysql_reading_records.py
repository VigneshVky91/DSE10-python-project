import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM dse10")

students = cursor.fetchall()

for student in students:
    print(f"Sid: {student[0]}, Sname: '{student[1]}', SAge: {student[2]}")