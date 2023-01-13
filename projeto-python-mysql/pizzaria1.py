import mysql.connector
import os


def pizzaria():
    print('================================================================')
    print('             ##     PIZZARIA GO-IT    ##')
    print('================================================================')


class Funcionario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha


pizzaria()
print('SEJA BEM VINDO FUNCIONARIO...')
usuario = input('DIGITE SEU USUARIO --> ')
os.system('cls')
pizzaria()
senha = input('DIGITE SUA SENHA --> ')

os.system('cls')
pizzaria()

print('        *CARDÁPIO DIGITAL PIZZARIO GO-IT*')


fucionario1 = Funcionario(usuario, senha)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

sql = "INSERT INTO funcionario (usuario, senha) VALUES ( %s, %s)"
val = (fucionario1.usuario, fucionario1.senha)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
