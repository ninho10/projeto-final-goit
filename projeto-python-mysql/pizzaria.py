# import getpass
import os



def pizzaria():
    print('================================================================')
    print('             SEJA BEM VINDO A PIZZARIA GO-IT')
    print('================================================================')


print('####################################################################')

pizzaria()

nome = input('Qual é seu fucionario --> ')
print('')
print(f'fucionario {nome} vamos criar usuario e senha ? ')
print('================================================================')
os.system('cls')

usuario = input(f'fucionario {nome} escolha seu nome de usuario --> ')
criarSenha = input('Escolha sua senha --> ')
print('================================================================')
os.system('cls')

print(f'{nome} parabéns..  *usuario e senha criados*')
print('Sua senha e particular não passe para ninguém')
print('')
print('================================================================')

while True:
    nomeUsuario = input('Qual e seu nome de usuario? --> ')
    senha = input("Digite sua senha: ")

    if (usuario != nomeUsuario) or (criarSenha != senha):
        print('tente novamente Usuario ou senha errado...')
        print('================================================================')

    if (usuario == nomeUsuario) and (criarSenha == senha):
        print('senha correta')
        break

os.system('cls')
pizzaria()

print('        *CARDÁPIO DIGITAL PIZZARIO GO-IT*')
