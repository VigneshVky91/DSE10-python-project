import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

print("Successfully connected with the DB")
no_of_recs = int(input("Input number of records to insert:"))

for i in range(no_of_recs):
    sid = int(input("Enter sid: "))
    sname = input("Enter sname: ")
    sage = int(input("Enter sage: "))
    cursor.execute(f"INSERT INTO dse10 VALUES ({sid}, '{sname}', {sage})")


connection.commit()

print(f"{no_of_recs} records have been stored in dse10 ...")
