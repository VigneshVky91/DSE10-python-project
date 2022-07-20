import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()
# cursor.execute("CREATE TABLE dse10 ( sid INT(3), sname VARCHAR(50), age INT(2));")

# print("Table dse10 created successfully under kit table")
cursor.execute("DESCRIBE dse10;")

result = cursor.fetchall()

for res in result:
    print(res[0], " : ", res[1])