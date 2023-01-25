import mysql.connector
from usuario import Usuario
from pizza import Pizza
from bebidas import Bebidas
from datetime import date
import os

today = date.today()
print("Today's date:", today)


def pizzaria():
    print('================================================================')
    print('             ##     PIZZARIA GO-IT    ##')
    print('================================================================')


def menu():
    print('''
               MENU:

               [1] - Iniciar Vendas
               [2] - Cadastra Usuario
               [3] - Total de Vendas
               [4] - Desligar

             ===================================''')


pizzaria()
menu()
n1 = input('Escolha uma opção: ')
os.system('cls')


if (n1 == '1'):
    pizzaria()

    while True:
        inputNomeUsuario = input('QUAL E SEU LONGIN--> ')

        inputSenha = input('QUAL É SUA SENHA --> ')

        cnx = mysql.connector.connect(
            host='localhost', database='pizzariagoit1', user='root', password='')
        cursor = cnx.cursor()
        cursor.execute(
            f'select * from tb_usuarios where login_usuario = "{inputNomeUsuario}"')

        queryResult = cursor.fetchone()

        cursor.close()
        cnx.close()

        usuario = Usuario(0, "", "", "")

        if queryResult == None:
            print("Usuario nao encontrado")
            break

        else:
            usuario = Usuario(
                queryResult[0], queryResult[2], queryResult[3], queryResult[1])

        if inputSenha == usuario.senha:
            print("logado com sucesso !")

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM tb_pizza")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            print(queryResult)

            pizzas = []

            for i in queryResult:

                pizzas.append(Pizza(i[0], i[1], i[2]))
                os.system('cls')
                pizzaria()

            for pizza in pizzas:
                print(f'{pizza.id}        {pizza.nome}                {pizza.preco}')
                print('------------------------------------------------------')

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()

            idPizzaSelecionada = input("Digite o numero pizza: ")

            cursor.execute("SELECT * FROM tb_bebidas")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            bebidas = []

            for i in queryResult:
                bebidas.append(Bebidas(i[0], i[1], i[3]))

            os.system('cls')
            pizzaria()

            for bebida in bebidas:
                print(
                    f'{bebida.id}        {bebida.nome}                {bebida.preco}')
                print('------------------------------------------------------')

            idBebidaSelecionada = input("Digite o numero da bebida: ")

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()

            add_venda = (
                f'INSERT INTO tb_vendas(id_pizza, totalpagar, nomecliente, id_bebidas, dataCompra ) VALUES("{pizzas[int(idPizzaSelecionada) - 1].id}", {pizzas[int(idPizzaSelecionada) - 1].preco + bebidas[int(idBebidaSelecionada)-1].preco}, "beatriz",{bebidas[int(idBebidaSelecionada)-1].id}, {date.today()})')

            cursor.execute(add_venda)
            cnx.commit()

            cursor.close()
            cnx.close()

        else:
            print("senha incorreta")
            break


if (n1 == '2'):
    os.system('cls')
    pizzaria()

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pizzariagoit1"
    )
    cursor = conexao.cursor()

    funcao = input('Qual é a função: ')
    login_usuario = input('Qual é o nome do usuario: ')
    senha_usuario = input('Qual é a senha: ')

    comando = f'INSERT INTO tb_usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()


elif (n1 == '3'):
    os.system('cls')
    pizzaria()
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pizzariagoit1"
    )
    cursor = conexao.cursor()

    comando = f'SELECT * FROM tb_vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()

else:
    os.system('cls')
    pizzaria()
    print('## FIM DO PROGRAMA ##')
