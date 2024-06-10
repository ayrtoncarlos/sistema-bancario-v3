from abc import ABC, abstractmethod


class Transacao(ABC):
    """
    Uma classe que representa uma transação.

    Métodos Abstratos
    -------
    valor():
        Retorna o valor de uma transação realizada.
    registrar(conta):
        Registra uma transação realizada.
    """

    @property
    @abstractmethod
    def valor(self):
        """Retorna o valor de uma transação realizada."""
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        """Registra uma transação realizada."""
        pass
