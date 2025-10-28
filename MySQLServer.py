# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # 1️⃣ Connect to MySQL server (without specifying a database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",            # replace with your MySQL username
        password="yourpassword" # replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # 2️⃣ Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # 3️⃣ Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
