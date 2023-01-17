import mysql.connector


print('Meus bancos de Dados')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

print('====================================================================')

print('Minha tabela funcionario')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM funcionario")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


print('====================================================================')

print('Minha tabela cliente')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cliente")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print('====================================================================')

print('Minha tabela pedido')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pedido")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
