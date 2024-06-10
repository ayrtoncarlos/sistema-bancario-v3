from interfaces.transacao import Transacao
from models.conta import Conta


class Cliente:
    """
    Uma classe que representa um cliente.

    Atributos
    ----------
    _endereco: str
        Endereço do cliente.
    _contas: list
        Lista de contas vinculadas ao cliente.

    Métodos
    -------
    endereco():
        Retorna o endereço do cliente.
    endereco(valor):
        Atualiza o endereço do cliente.
    contas():
        Retorna as contas vinculadas ao cliente.
    contas(conta):
        Atualiza a lista de contas do cliente.
    realizar_transacao(conta, transacao):
        Registra uma transação realizada em uma conta vinculada ao cliente.

    Métodos Mágicos
    -------
    __init__(endereco):
        Constrói todos os atributos necessários para o objeto Cliente.
    """

    def __init__(self, endereco: str) -> None:
        """
        Constrói todos os atributos necessários para o objeto Cliente.

        Parâmetros
        ----------
        endereco : str
            Endereço do cliente.
        """
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self) -> str:
        """Retorna o endereço do cliente."""
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        """Atualiza o endereço do cliente."""
        self._endereco = endereco

    @property
    def contas(self) -> list:
        """Retorna as contas vinculadas ao cliente."""
        return self._contas

    @contas.setter
    def contas(self, conta) -> None:
        """Atualiza a lista de contas do cliente."""
        self._contas.append(conta)

    @staticmethod
    def realizar_transacao(conta: Conta, transacao: Transacao) -> None:
        """Registra uma transação realizada em uma conta vinculada ao cliente."""
        transacao.registrar(conta)
