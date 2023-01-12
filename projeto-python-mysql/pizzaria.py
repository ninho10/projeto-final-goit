
def pizzaria():
    print('================================================================')
    print('             SEJA BEM VINDO A PIZZARIA GO-IT')
    print('================================================================')


pizzaria()

nome = input('Qual é seu nome --> ')
print('')
print(f'{nome} vamos criar usuario e senha ')
print('================================================================')


usuario = input('Escolha seu nome de usuario --> ')
criarSenha = input('Escolha sua senha --> ')
print('================================================================')

while True:
    nomeUsuario = input('Qual e seu nome de usuario? --> ')
    senha = input('Qual e sua senha? --> ')

    if (usuario != nomeUsuario) or (criarSenha != senha):
        print('tente novamente Usuario ou senha errado...')
        print('================================================================')

    if (usuario == nomeUsuario) and (criarSenha == senha):
        print('senha correta')
        break


pizzaria()

print('APP PIZZA GO-IT')
