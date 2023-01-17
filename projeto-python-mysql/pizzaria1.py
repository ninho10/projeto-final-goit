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
funcionario = input('FUCIONARIO VOCÊ TEM USUARIO (S) SIM OU (N) NÃO --> ')


if funcionario == 'n':
    print('SEJA BEM VINDO FUNCIONARIO...')
    print('FUMCIONARIO VAMOS CRIAR USUARIO E SENHA')
    usuario = input('CRIER SEU USUARIO --> ')
    os.system('cls')
    pizzaria()
    senha = input('CRIER SUA SENHA --> ')

    fucionario1 = Funcionario(usuario, senha)

    # MYSQL funcionario
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


if funcionario == 's':
    usuarioCadastrado = input('DIGITE SEU USUARIO --> ')
    os.system('cls')
    pizzaria()
    senhaCadastrada = input('DIGITE SUA SENHA --> ')


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
print('  Musarela     30.00               coca cola      ')
print('  calabresa    30.00               Fanta uva      ')
print('  portuguesa   30.00               Fanta Larranja ')
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
    f'O pedido do {cliente.nome} ficou uma pizza {pedido.pizza} é um refrigerante {pedido.refrigerante}')
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
