# Importing the driver into the python code
import mysql.connector

# Establishing connection and storing the connection into a variable
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port="3306"
)

# Creating cursor
cursor = connection.cursor()

# Write query to create database
cursor.execute("CREATE DATABASE kit")
print("Database created successfully...")
