import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="db_user",
    password="877bd4222b3f73d92b8c"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()

    create_db = "CREATE DATABASE alx_book_store"

    mycursor.execute(create_db)

except mysql.connector.Error as err:
    print(f"Error: {err.msg}")

else:
    print("Database 'alx_book_store' created successfully!")

finally:
    mycursor.close()
    mydb.close()

