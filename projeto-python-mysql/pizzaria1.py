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
print('FUNCIONARIO DIGITE SEU USUARIO É SENHA')
print('')
usuario = input('DIGITE NOME DE USUARIO --> ')
os.system('cls')
pizzaria()
senha = input('DIGITE SUA SENHA --> ')


fucionario1 = Funcionario(usuario, senha)

# MYSQL funcionario
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

sql = "INSERT IGNORE INTO funcionario (usuario, senha) VALUES ( %s, %s)"
val = (fucionario1.usuario, fucionario1.senha)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# ==================================================================================================

os.system('cls')
pizzaria()


class Cliente:
    def __init__(self, nome, celular, endereco):
        self.nome = nome
        self.celular = celular
        self.endereco = endereco


nome = input('QUAL E O NOME DO CLIENTE --> ')
celular = input('QUAL E O CELULAR DO CLIENTE --> ')
endereco = input('QUAL O ENDEREÇO DO CLIENTE --> ')

cliente = Cliente(nome, celular, endereco)

# MYSQL cliente
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

sql = "INSERT INTO cliente (id, nome, celular, endereco) VALUES (0, %s, %s, %s)"
val = (cliente.nome, cliente.celular, cliente.endereco)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# ==================================================================================================

os.system('cls')
pizzaria()

print('        *CARDÁPIO DIGITAL PIZZARIO GO-IT*')
print('==================================================')
print('  pizzas       valor             Refrigerentes    ')
print('')
print('  musarela     30.00               coca cola      ')
print('  calabresa    30.00               fanta uva      ')
print('  portuguesa   30.00               fanta larranja ')
print('==================================================')


class Pedido:
    def __init__(self, pizza, refrigerante, valor):
        self.pizza = pizza
        self.refrigerante = refrigerante
        self.valor = valor


pizza = input('QUAL SABOR DA PIZZA --> ')
refrigerante = input('QUAL SABOR DO REFRIGERANTE --> ')
valor = int(input('QUAL E O VALOR --> '))


pedido = Pedido(pizza, refrigerante, valor)

os.system('cls')
pizzaria()

print(
    f'Cliente {cliente.nome} ficou uma pizza {pedido.pizza} é um refrigerante {pedido.refrigerante}')
print(f'total apagar {pedido.valor}')


# MYSQL pedido
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizzaria"
)

mycursor = mydb.cursor()

sql = "INSERT INTO pedido (id, pizza, refrigerante, valor) VALUES (0, %s, %s, %s)"
val = (pedido.pizza, pedido.refrigerante, pedido.valor)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
