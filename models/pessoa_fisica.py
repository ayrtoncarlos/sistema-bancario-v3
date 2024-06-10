from models.cliente import Cliente


class PessoaFisica(Cliente):
    """
    Uma classe que representa uma pessoa física.

    Atributos
    ----------
    _nome : str
        nome da pessoa.
    _cpf : str
        CPF da pessoa.
    _data_nascimento: str
        Data de nascimento da pessoa.
    _endereco: str
        Endereço da pessoa.

    Métodos
    -------
    nome():
        Retorna o nome da pessoa.
    nome(valor):
        Atualiza o nome da pessoa.
    cpf():
        Retorna o CPF da pessoa.
    cpf(valor):
        Atualiza o CPF da pessoa.
    data_nascimento():
        Retorna a data de nascimento da pessoa.
    data_nascimento(valor):
        Atualiza a data de nascimento da pessoa.
    endereco():
        Retorna o endereço da pessoa.
    endereco(valor):
        Atualiza o endereço da pessoa.

    Métodos Mágicos
    -------
    __init__(nome, cpf, data_nascimento, endereco):
        Constrói todos os atributos necessários para o objeto PessoaFisica.
    __str__():
        Retorna a representação str do objeto PessoaFisica.
    """

    def __init__(
        self, nome: str, cpf: str, data_nascimento: str, endereco: str
    ) -> None:
        """
        Constrói todos os atributos necessários para o objeto PessoaFisica.

        Parâmetros
        ----------
        nome : str
            nome da pessoa.
        cpf : str
            CPF da pessoa.
        data_nascimento: str
            Data de nascimento da pessoa.
        endereco: str
            Endereço da pessoa.
        """
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco

    @property
    def nome(self) -> str:
        """Retorna o nome da pessoa."""
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        """Atualiza o nome da pessoa."""
        self._nome = valor

    @property
    def cpf(self) -> str:
        """Retorna o CPF da pessoa."""
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str) -> None:
        """Atualiza o CPF da pessoa."""
        self._cpf = valor

    @property
    def data_nascimento(self) -> str:
        """Retorna a data de nascimento da pessoa."""
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor: str) -> None:
        """Atualiza a data de nascimento da pessoa."""
        self._data_nascimento = valor

    @property
    def endereco(self) -> str:
        """Retorna o endereço da pessoa."""
        return self._endereco

    @endereco.setter
    def endereco(self, valor: str) -> None:
        """Atualiza o endereço da pessoa."""
        self._endereco = valor

    def __str__(self) -> str:
        """Retorna a representação str do objeto PessoaFisica."""
        return f"Nome:\t\t\t\t{self._nome}\nCPF:\t\t\t\t{self._cpf}\nData Nascimento:\t{self._data_nascimento}\nEndereço:\t\t\t{self._endereco}"
