import textwrap

from models.cliente import Cliente
from models.conta import Conta
from models.conta_corrente import ContaCorrente
from models.pessoa_fisica import PessoaFisica
from services.deposito import Deposito
from services.saque import Saque


def show_menu():
    """Mostra o menu e suas opções."""
    menu = f"""\n
    {" MENU ".center(40, "#")}
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [lcl]\tListar Clientes
    [nu]\tNovo Usuário
    [q]\t\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf: str, clientes: list) -> Cliente:
    """Retorna um Cliente se caso for encontrado, senão retorna None."""
    clientes_filtrados = [
        cliente for cliente in clientes if cliente.cpf == cpf
    ]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente: Cliente) -> Conta:
    """Retorna a Conta do Cliente, caso ele possua uma."""
    if not cliente.contas:
        print(" Cliente não possui conta! ".center(40, "#"))
    return cliente.contas[0]


def depositar(clientes: list) -> None:
    """Realiza um depósito para o Cliente informado."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" Cliente não encontrado! ".center(40, "#"))
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes: list) -> None:
    """Realiza um saque para o Cliente informado."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" Cliente não encontrado! ".center(40, "#"))
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: list) -> None:
    """Exibe o extrato do Cliente informado."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" Cliente não encontrado! ".center(40, "#"))
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print(" EXTRATO ".center(40, "#"))

    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for index, transacao in enumerate(transacoes):
            print(index + 1, transacao)

    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("".center(40, "#"))


def criar_cliente(clientes: list) -> None:
    """Realiza a criação de um Cliente, caso não esteja cadastrado no sistema."""
    cpf = input("Informe o CPF (somente numeros): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(" Já existe cliente com esse CPF! ".center(40, "#"))
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Infome a data de nascimento (dia/mês/ano): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print(" Cliente criado com sucesso! ".center(40, "#"))


def criar_conta(numero_conta: int, clientes: list, contas: list) -> None:
    """Realiza a criação de uma Conta, caso o Cliente informado já esteja cadastrado no sistema e não tenha uma."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" Cliente não encontrado! ".center(40, "#"))
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(" Conta criada com sucesso! ".center(40, "#"))


def listar_clientes(clientes: list) -> None:
    """Lista todos os clientes existentes no sistema."""
    for cliente in clientes:
        print("".center(100, "#"))
        print(textwrap.dedent(str(cliente)))


def listar_contas(contas: list) -> None:
    """Lista todas as contas existentes no sistema."""
    for conta in contas:
        print("".center(100, "#"))
        print(textwrap.dedent(str(conta)))


def main() -> None:
    """Método de inicialização do sistema."""
    clientes = []
    contas = []

    while True:
        opcao = show_menu().lower().strip()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lcl":
            listar_clientes(clientes)

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida! Por favor selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()
