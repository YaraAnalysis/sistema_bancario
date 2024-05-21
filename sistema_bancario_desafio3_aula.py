from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class CLiente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        pass


class PessoaFisica(Cliente):
    pass


class Conta:
    pass


class ContaCorrente(Conta):
    pass


class Historico:
    pass


class Transacao(ABC):
    pass


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass
