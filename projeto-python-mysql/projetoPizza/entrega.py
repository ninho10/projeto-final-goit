class Entrega:
    def __init__(self, id_entrega, formaEntrega, formaPagamento):
        self.__id_entrega: id_entrega
        self.__formaEntrega: formaEntrega
        self.__formaPagamento: formaPagamento


@property
def id_entrega(self):
    return self.__id_entrega


@id_entrega.setter
def id_entrega(self, id_entrega):
    self.__id_entrega = id_entrega


@property
def formaEntrega(self):
    return self.__formaEntrega


@formaEntrega.setter
def formaEntrega(self, formaEntrega):
    self.__formaEntrega = formaEntrega


@property
def formaPagamento(self):
    return self.__formaPagamento


@formaPagamento.setter
def formaPagamento(self, formaPagamento):
    self.__formaPagamento = formaPagamento
