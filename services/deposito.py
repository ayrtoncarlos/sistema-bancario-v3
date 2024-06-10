from datetime import datetime

from interfaces.transacao import Transacao
from models.conta import Conta


class Deposito(Transacao):
    """
    Uma classe que representa um depósito.

    Atributos
    ----------
    _valor: float
        Valor para depositar.
    _data: str
        Data de depósito.

    Métodos
    -------
    valor():
        Retorna o valor do depósito.
    registrar(conta):
        Registra uma transação de depósito no histórico da conta, caso sucesso.

    Métodos Mágicos
    -------
    __init__(valor):
        Constrói todos os atributos necessários para o objeto Deposito.
    __str__():
        Retorna a representação str do objeto Deposito.
    """

    def __init__(self, valor: float) -> None:
        """
        Constrói todos os atributos necessários para o objeto Deposito.

        Parâmetros
        ----------
        valor : float
            Valor para depositar.
        """
        super().__init__()
        self._valor = valor
        self._data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def valor(self) -> float:
        """Retorna o valor do depósito."""
        return self._valor

    def registrar(self, conta: Conta) -> None:
        """Registra uma transação de depósito no histórico da conta, caso sucesso."""
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.transacoes.append(self)

    def __str__(self) -> str:
        """Retorna a representação str do objeto Deposito."""
        return f"Tipo: {self.__class__.__name__} | Valor: {self._valor} | Data: {self._data}"
