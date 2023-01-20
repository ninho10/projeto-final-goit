import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)
cursor = conexao.cursor()

comando = f'SELECT * FROM usuarios'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()
