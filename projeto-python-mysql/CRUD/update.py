import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)
cursor = conexao.cursor()

sabor = "quatro queijos"
valor = 40

comando = f'UPDATE pizza SET valor = {valor} WHERE sabor = "{sabor}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
