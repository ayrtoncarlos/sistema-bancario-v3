from datetime import datetime

from interfaces.transacao import Transacao
from models.conta import Conta


class Saque(Transacao):
    """
    Uma classe que representa um saque.

    Atributos
    ----------
    _valor: float
        Valor para sacar.
    _data: str
        Data de saque.

    Métodos
    -------
    valor():
        Retorna o valor do saque.
    registrar(conta):
        Registra uma transação de saque no histórico da conta, caso sucesso.

    Métodos Mágicos
    -------
    __init__(valor):
        Constrói todos os atributos necessários para o objeto Saque.
    __str__():
        Retorna a representação str do objeto Saque.
    """

    def __init__(self, valor: float) -> None:
        """
        Constrói todos os atributos necessários para o objeto Saque.

        Parâmetros
        ----------
        valor : float
            Valor para sacar.
        """
        super().__init__()
        self._valor = valor
        self._data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def valor(self) -> float:
        """Retorna o valor do saque."""
        return self._valor

    def registrar(self, conta: Conta) -> None:
        """Registra uma transação de saque no histórico da conta, caso sucesso."""
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.transacoes.append(self)

    def __str__(self) -> str:
        """Retorna a representação str do objeto Saque."""
        return f"Tipo: {self.__class__.__name__} | Valor: {self._valor} | Data: {self._data}"
