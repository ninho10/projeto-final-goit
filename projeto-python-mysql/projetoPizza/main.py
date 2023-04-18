import mysql.connector          # importando o banco de dados
from usuario import Usuario
from pizza import Pizza          # importando class da linha 2 até 5
from bebidas import Bebidas
from vendas import Vendas
from datetime import date        # importando data
import getpass                   # gestpass para esconder senha
import os                        # para limpar tela


today = date.today()
print("Today's date:", today)          # estou chamando é mostrando a data

# função pizzaria para guarda a marca do cliente


def pizzaria():
    print('================================================================')
    print('             ##     PIZZARIA GO-IT    ##')
    print('================================================================')

# função menu para guarda o menu do código onde esse menu tem 4 opção


def menu():
    print('''
               MENU:

               [1] - Iniciar Vendas
               [2] - Cadastrar Usuario
               [3] - Total de Vendas
               [4] - Desligar

             ===================================''')


# chamando função pizzaria e menu
pizzaria()
menu()
escolhaMenu = input('Escolha uma opção: ')  # escolher uma opção do menur
os.system('cls')
cont01 = 0   # variavel para usar como contador
cont02 = 0
if (escolhaMenu == '1'):

    while True:  # loop de repetição, enquanto for verdadeira vai rodar
        os.system('cls')
        pizzaria()

        inputNomeUsuario = input('Seu login--> ')

        # chamando o getpass, senha escondida
        inputSenha = getpass.getpass('Sua senha --> ')

        # linha 55 áte 64 conexão com o banco pizzariagoit1 na tabela tb_usuarios
        cnx = mysql.connector.connect(
            host='localhost', database='pizzariagoit1', user='root', password='')
        cursor = cnx.cursor()
        cursor.execute(
            f'select * from tb_usuarios where login_usuario = "{inputNomeUsuario}"')

        queryResult = cursor.fetchone()

        cursor.close()
        cnx.close()
        # chamando a class Usuario, modificando para objeto
        usuario = Usuario(0, "", "", "")

        if queryResult == None:     # usuaria sendo incorreto cai nesse if
            erroUsuario = input("** Usuario incorreto **  [enter]")
            cont01 = cont01 + 1     # somando o contador chegar a 3 sai do programa
            if cont01 == 3:
                break

        else:  # usuario correto cai nesse else
            usuario = Usuario(
                queryResult[0], queryResult[2], queryResult[3], queryResult[1])

        if inputSenha == usuario.senha:  # senha correta cai nesse if
            # usuario e senha correta roda o programa
            print("logado com sucesso !")

            # linha 82 áte 93 conexão com o banco pizzariagoit1 na tabela tb_pizza
            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM tb_pizza")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            print(queryResult)
            # uma lista
            pizzas = []
            # para pegar todo o conteúdo
            for i in queryResult:
                # coloca conteúdo na lista
                pizzas.append(Pizza(i[0], i[1], i[2]))
                os.system('cls')
                pizzaria()
             # printa conteúdo
            for pizza in pizzas:
                print(f'{pizza.id}        {pizza.nome}                {pizza.preco}')
                print('------------------------------------------------------')

             # linha 108 áte 121 conexão com o banco pizzariagoit1 na tabela tb_bebidas
            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()

            idPizzaSelecionada = input(" Id da pizza --> ")

            cursor.execute("SELECT * FROM tb_bebidas")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            bebidas = []

            for i in queryResult:
                bebidas.append(Bebidas(i[0], i[1], i[2]))

            os.system('cls')
            pizzaria()

            for bebida in bebidas:
                print(
                    f'{bebida.id}        {bebida.nome}                {bebida.preco}')
                print('------------------------------------------------------')

            idBebidaSelecionada = input("Id bebida --> ")
            # linha 137 áte 153 conexão com o banco pizzariagoit1 na tabela tb_vendas

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='')
            cursor = cnx.cursor()

            nomeCliente = input('Nome do cliente --> ')
            dataPedido = date.today()
            # colocando tudo que foi vendido no banco de dados tabala tb_venda
            add_venda = (
                f'INSERT INTO tb_vendas(id_pizza, totalpagar, nomecliente, id_bebidas, datavenda ) VALUES("{pizzas[int(idPizzaSelecionada) - 1].id}", {pizzas[int(idPizzaSelecionada) - 1].preco + bebidas[int(idBebidaSelecionada)-1].preco}, "{nomeCliente}",{bebidas[int(idBebidaSelecionada)-1].id}, now())')

            vendaOk = input('venda ok.. [enter]')

            cursor.execute(add_venda)
            cnx.commit()

            cursor.close()
            cnx.close()

            # esse if e para continuar vendedo ou termina o programa
            continuarVenda = input(
                ' Continuar vendendo [s]sim ou [n]não ? --> ')
            if continuarVenda == 'n':
                break

        else:   # cai nesse else senha incorretas
            erroSenha = input("** Senha incorreta **  [enter]")
            print('--------------------------------------------')
            print('')
            cont02 = cont02 + 1
            nomeroErros = input(
                f'Maximo de erro 3X usuario {cont01}X é senha {cont02}X [enter]')
            if cont02 == 3:
                break

# menu para cadastrar novos usuarios
if (escolhaMenu == '2'):
    os.system('cls')
    pizzaria()

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pizzariagoit1"
    )
    cursor = conexao.cursor()

    # passar informação do novo usuario
    funcao = input('função --> ')
    login_usuario = input('Login do usuario --> ')
    senha_usuario = input('Senha nova --> ')

    comando = f'INSERT INTO tb_usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

# mostra o total de vendas
elif (escolhaMenu == '3'):
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

    vendas = []

    for i in resultado:
        vendas.append(Vendas(i[0], i[1], i[2], i[3], i[4], i[5]))

    cursor.close()
    conexao.close()

    os.system('cls')

    print('id venda      | id bebida     | id pizza     | valor     | clinte      | data     ')
    for venda in vendas:
        print(f'{venda.id}             | {venda.idBebida}             | {venda.idPizza}            | {venda.valor}      | {venda.cliente}       | {venda.data}')
    print('------------------------------------------------------')

# quando cai nesse else é o fim do programa
else:
    os.system('cls')
    pizzaria()
    print('## FIM DO PROGRAMA ##')

