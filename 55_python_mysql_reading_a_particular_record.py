import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

sid = int(input("Input the sid of the record to be found: "))

cursor.execute(f"SELECT * FROM dse10 WHERE sid = {sid}")

students = cursor.fetchall()

for student in students:
    print(f"Sid: {student[0]}, Sname: '{student[1]}', SAge: {student[2]}")