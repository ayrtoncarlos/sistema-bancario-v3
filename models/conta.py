from services.historico import Historico


class Conta:
    """
    Uma classe que representa uma conta.

    Constante
    ----------
    AGENCIA: tuple
        Número da agência.

    Atributos
    ----------
    _numero : int
        número da conta.
    _cliente: Cliente
        Cliente que será vinculado a nova conta.
    _saldo: float
        valor de saldo da conta.
    _historico: Historico
        Histórico de movimentações da conta.

    Métodos
    -------
    nova_conta(cliente, numero):
        Retorna uma conta nova para o cliente.
    saldo():
        Retorna o saldo da conta.
    saldo(valor):
        Atualiza o valor do saldo.
    numero():
        Retorna o número da conta.
    agencia():
        Retorna o número da agência.
    cliente():
        Retorna o cliente vinculado a conta.
    historico():
        Retorna o histórico de movimentações da conta.
    sacar(valor):
        Realiza um saque na conta se valor informado for válido.
    depositar(valor):
        Realiza um depósito na conta se valor informado for válido.


    Métodos Mágicos
    -------
    __init__(numero, cliente):
        Constrói todos os atributos necessários para o objeto Conta.
    """

    AGENCIA = ("0001",)

    def __init__(self, numero: int, cliente) -> None:
        """
        Constrói todos os atributos necessários para o objeto Conta.

        Parâmetros
        ----------
        numero : int
            número da conta.
        cliente: Cliente
            Cliente que será vinculado a nova conta.
        """
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        """Retorna uma conta nova para o cliente."""
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        """Retorna o saldo da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        """Atualiza o valor do saldo."""
        self._saldo = valor

    @property
    def numero(self) -> int:
        """Retorna o número da conta."""
        return self._numero

    @property
    def agencia(self) -> str:
        """Retorna o número da agência."""
        return self.AGENCIA[0]

    @property
    def cliente(self):
        """Retorna o cliente vinculado a conta."""
        return self._cliente

    @property
    def historico(self) -> Historico:
        """Retorna o histórico de movimentações da conta."""
        return self._historico

    def sacar(self, valor: float) -> bool:
        """Realiza um saque na conta se valor informado for válido."""
        excedeu_saldo = valor > self._saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print(" Saque realizado com sucesso! ".center(40, "#"))
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor: float) -> bool:
        """Realiza um depósito na conta se valor informado for válido."""
        if valor > 0:
            self._saldo += valor
            print(" Depósito realizado com sucesso! ".center(40, "#"))
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

        return True
