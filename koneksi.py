import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="corona_db"
    )
mycursor = mydb.cursor()