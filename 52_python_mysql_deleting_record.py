import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

sid_to_delete = int(input("Input the sid of the record to be deleted: "))

cursor.execute(f"DELETE FROM dse10 WHERE sid = {sid_to_delete}")

connection.commit()