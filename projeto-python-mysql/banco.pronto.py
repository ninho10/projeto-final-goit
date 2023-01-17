import mysql.connector
import pizzaria1

fucionario1 = Funcionario(usuario, senha)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

sql = "INSERT INTO funcionario (id, usuario, senha) VALUES (0, %s, %s)"
val = (fucionario1.usuario, fucionario1.senha)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")