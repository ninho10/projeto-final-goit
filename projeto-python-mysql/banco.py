import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE funcionario (usuario VARCHAR(20) PRIMARY KEY, senha VARCHAR(20))")
