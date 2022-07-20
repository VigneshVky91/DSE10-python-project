import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)

cursor = connection.cursor()

sid_to_update = int(input("Input the sid of the record to be updated: "))
sname_to_update = input("Input the updated name: ")

cursor.execute(f"UPDATE dse10 SET sname = '{sname_to_update}' WHERE sid = {sid_to_update}")
print("Record updated successfully...")

connection.commit()

