class Vendas:
    def __init__(self, id_usuarios, id_vendas,  id_bebidas, id_pizza,  id_entrega, nomeCliente, totalPagar, qtdeTotalPizzas, qtdeTotalBebidas, dataCompra):
        self.__id_usuarios: id_usuarios
        self.__id_vendas: id_vendas
        self.__id_bebidas: id_bebidas
        self.__id_pizza: id_pizza
        self.__id_entrega: id_entrega
        self.__nomeCliente: nomeCliente
        self.__totalPagar: totalPagar
        self.__qtdeTotalPizzas: qtdeTotalPizzas
        self.__qtdeTotalBebidas: qtdeTotalBebidas
        self.__dataCompra: dataCompra


@property
def id_usuarios(self):
    return self.__id_usuarios


@id_usuarios.setter
def id_usuarios(self, id_usuarios):
    self.__id_usuarios = id_usuarios


@property
def id_vendas(self):
    return self.__id_vendas


@id_vendas.setter
def id_vendas(self, id_vendas):
    self.__id_vendas = id_vendas


@property
def id_bebidas(self):
    return self.__id_bebidas


@id_bebidas.setter
def id_bebidas(self, id_bebidas):
    self.__id_bebidas = id_bebidas


@property
def id_pizza(self):
    return self.__id_pizza


@id_pizza.setter
def id_pizza(self, id_pizza):
    self.__id_pizza = id_pizza


@property
def id_entrega(self):
    return self.__id_entrega


@id_entrega.setter
def id_entrega(self, id_entrega):
    self.__id_entrega = id_entrega


@property
def nomeCliente(self):
    return self.__nomeCliente


@nomeCliente.setter
def nomeCliente(self, nomeCliente):
    self.__nomeCliente = nomeCliente


@property
def totalPagar(self):
    return self.__totalPagar


@totalPagar.setter
def totalPagar(self, totalPagar):
    self.__totalPagar = totalPagar


@property
def qtdeTotalPizzas(self):
    return self.__qtdeTotalPizzas


@qtdeTotalPizzas.setter
def qtdeTotalPizzas(self, qtdeTotalPizzas):
    self.__qtdeTotalPizzas = qtdeTotalPizzas


@property
def qtdeTotalBebidas(self):
    return self.__qtdeTotalBebidas


@qtdeTotalBebidas.setter
def nomecliente(self, qtdeTotalBebidas):
    self.__qtdeTotalBebidas = qtdeTotalBebidas


@property
def dataCompra(self):
    return self.__dataCompra


@dataCompra.setter
def dataCompra(self, dataCompra):
    self.__dataCompra = dataCompra
