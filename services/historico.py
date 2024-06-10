from interfaces.transacao import Transacao


class Historico:
    """
    Uma classe que representa um histórico.

    Atributos
    ----------
    _transacoes: list
        Lista de transações.

    Métodos
    -------
    transacoes():
        Retorna todas as transações realizadas em uma conta.
    transacoes(transacao):
        Adiciona uma nova transação realizada em uma conta.

    Métodos Mágicos
    -------
    __init__():
        Constrói todos os atributos necessários para o objeto Historico.
    """

    def __init__(self) -> None:
        """Constrói todos os atributos necessários para o objeto Historico."""
        self._transacoes = []

    @property
    def transacoes(self) -> list:
        """Retorna todas as transações realizadas em uma conta."""
        return self._transacoes

    @transacoes.setter
    def transacoes(self, transacao: Transacao) -> None:
        """Adiciona uma nova transação realizada em uma conta."""
        self._transacoes.append(transacao)
