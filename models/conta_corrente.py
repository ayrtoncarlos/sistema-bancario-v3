from models.cliente import Cliente
from models.conta import Conta
from services.saque import Saque


class ContaCorrente(Conta):
    """
    Uma classe que representa uma conta corrente.

    Constantes
    ----------
    LIMITE: typle
        Valor limite de um saque.
    LIMITE_SAQUES:
        Número limite de saques diário.

    Atributos
    ----------
    _numero : int
        número da conta.
    _cliente : Cliente
        Cliente que será vinculado a nova conta.

    Métodos
    -------
    limite():
        Retorna o valor limite de um saque.
    limite_saques():
        Retorna o valor limite de saques diário.
    sacar(valor):
        Valida se um saque pode ser realizado.

    Métodos Mágicos
    -------
    __init__(numero, cliente):
        Constrói todos os atributos necessários para o objeto ContaCorrente.
    __str__():
        Retorna a representação str do objeto conta corrente.
    """

    LIMITE = (500,)
    LIMITE_SAQUES = (3,)

    def __init__(self, numero: int, cliente: Cliente) -> None:
        """
        Constrói todos os atributos necessários para o objeto ContaCorrente.

        Parâmetros
        ----------
        numero : str
            número da conta.
        cliente : Cliente
            Cliente que será vinculado a nova conta.
        """
        super().__init__(numero, cliente)

    @property
    def limite(self) -> int:
        """Retorna o valor limite de um saque."""
        return self.LIMITE[0]

    @property
    def limite_saques(self) -> int:
        """Retorna o valor limite de saques diário."""
        return self.LIMITE_SAQUES[0]

    def sacar(self, valor: float) -> bool:
        """Valida se um saque pode ser realizado."""
        excedeu_limite = valor > self.limite
        excedeu_saques = (
            len(
                [
                    transacao
                    for transacao in self.historico.transacoes
                    if transacao.__class__.__name__ == Saque.__name__
                ]
            )
            >= self.limite_saques
        )

        if excedeu_limite:
            print(
                f"Operação falhou! O valor do saque excede o limite de R$ {self.limite}."
            )
        elif excedeu_saques:
            print(
                f"Operação falhou! Número máximo de saques excedido.\nLimite de saques diário é: {self.limite_saques}."
            )
        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        """Retorna a representação str do objeto ContaCorrente."""
        return f"Agência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"
