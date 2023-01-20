class Usuarios:
    def __init__(self, id_usuarios, funcao, login_usuario, senha_usuario):
        self.__id_usuarios: id_usuarios
        self.__funcao: funcao
        self.__login_usuario: login_usuario
        self.__senha_usuario: senha_usuario


@property
def id_usuarios(self):
    return self.__id_usuarios


@id_usuarios.setter
def id_usuarios(self, id_usuarios):
    self.__id_usuarios = id_usuarios


@property
def funcao(self):
    return self.__funcao


@funcao.setter
def funcao(self, funcao):
    self.__funcao = funcao


@property
def login_usuario(self):
    return self.__login_usuario


@login_usuario.setter
def login_usuario(self, login_usuario):
    self.__login_usuario = login_usuario


@property
def senha_usuario(self):
    return self.__senha_usuario


@senha_usuario.setter
def senha_usuario(self, senha_usuario):
    self.__senha_usuario = senha_usuario
