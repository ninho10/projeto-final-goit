'''
import mysql.connector
import read
import update
import delete
import mysql.connector
import os


def pizzaria():
    print('================================================================')
    print('             ##     PIZZARIA GO-IT    ##')
    print('================================================================')


class Usuarios:
    def __init__(self, funcao, login_usuario, senha_usuario):
        self.funcao = funcao
        self.login_usuario = login_usuario
        self.senha_usuario = senha_usuario


pizzaria()

print('SEJA BEM VINDO FUNCIONARIO...')
funcao = input('QUAL É SUA FUNÇÃO --> ')

print('FUNCIONARIO DIGITE SEU USUARIO É SENHA')
print('')
login_usuario = input('DIGITE NOME DE USUARIO --> ')
os.system('cls')
pizzaria()
senha_usuario = input('DIGITE SUA SENHA --> ')


usuarios = Usuarios(funcao, login_usuario, senha_usuario)


# ==================================================================================================

os.system('cls')
pizzaria()

print('        *CARDÁPIO DIGITAL PIZZARIO GO-IT*')
print('==================================================')
print('  pizzas       valor    Refrigerentes   valor')
print('')
print('  musarela     30.00    coca cola       10.00')
print('  calabresa    30.00    fanta uva       10.00')
print('  portuguesa   30.00    fanta larranja  10.00')
print('==================================================')


class Pizza:
    def __init__(self, sabor, valor):
        self.sabor = sabor
        self.valor = valor


sabor = input('QUAL SABOR DA PIZZA --> ')
valor = int(input('QUAL E O VALOR --> '))


pizza = Pizza(sabor, valor)

# =================================================================================
os.system('cls')
pizzaria()

print('        *CARDÁPIO DIGITAL PIZZARIO GO-IT*')
print('==================================================')
print('  pizzas       valor    Refrigerentes   valor')
print('')
print('  musarela     30.00    coca cola       10.00')
print('  calabresa    30.00    fanta uva       10.00')
print('  portuguesa   30.00    fanta larranja  10.00')
print('==================================================')


class Bebidas:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


nome = input('QUAL BEBIDA --> ')
preco = input('VALOR DA BEBIDA --> ')

bebidas = Bebidas(nome, preco)


# ======================================================================================


# class Vendas:
# def __init__(self, nomeCliente,  totalPagar, endereco):
# self.nomeCliente  = nomeCliente
# self.totalPagar = totalPagar
# self.endereco = endereco

os.system('cls')
pizzaria()

nomeCliente = input('QUAL E O NOME DO CLIENTE --> ')
totalPagar = pizza.valor + bebidas.preco
idPizza = 1
idBebida = 1
idUsuario = 1

os.system('cls')
print(f'{nomeCliente} o valor total ficou ${totalPagar}')
print('======================================================================')
'''
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)
cursor = conexao.cursor()

funcao = "balconista"
login_usuario = "roberto"
senha_usuario = "1010"

sabor = "musarela"
valor = 30

nome = "coca cola"
preco = 10

nomeCliente = "rafael"
totalPagar = valor + preco
idPizza = 1
idBebida = 1
idUsuario = 1

comando = f'INSERT INTO usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")'
comando1 = f'INSERT INTO pizza (sabor, valor) VALUES ("{sabor}", {valor})'
comando2 = f'INSERT INTO bebidas (nome, preco) VALUES ("{nome}", {preco})'
comando3 = f'INSERT INTO vendas (nomeCliente, totalPagar, idPizza, idBebida, idUsuario) VALUES ("{nomeCliente}", {totalPagar}, {idPizza}, {idBebida}, {idUsuario})'

cursor.execute(comando)
cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(comando3)

conexao.commit()

cursor.close()
conexao.close()
