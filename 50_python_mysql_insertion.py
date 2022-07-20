import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

cursor.execute("INSERT INTO dse10 VALUES (%s, %s, %s);", (1234, "Panha", 20))
print("Record inserted successfully...")

connection.commit()