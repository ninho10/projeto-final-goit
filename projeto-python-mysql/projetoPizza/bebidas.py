class Bebidas:
    def __init__(self, id_bebidas, nome, qtdDisponivel, preco):
        self.__id_bebidas: id_bebidas
        self.__nome: nome
        self.__qtdDisponivel: qtdDisponivel
        self.__preco: preco


@property
def id_bebidas(self):
    return self.__id_bebidas


@id_bebidas.setter
def id_bebidas(self, id_bebidas):
    self.__id_bebidas = id_bebidas


@property
def qtdDisponivel(self):
    return self.__qtdDisponivel


@qtdDisponivel.setter
def qtdDisponivel(self, qtdDisponivel):
    self.__qtdDisponivel = qtdDisponivel


@property
def preco(self):
    return self.__preco


@preco.setter
def preco(self, preco):
    self.__preco = preco


@property
def nome(self):
    return self.__nome


@nome.setter
def nome(self, nome):
    self.__nome = nome
