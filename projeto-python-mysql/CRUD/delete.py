import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)
cursor = conexao.cursor()

preco = 10


comando = f'DELETE FROM bebidas WHERE preco = "{10}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
