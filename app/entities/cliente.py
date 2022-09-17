"""Cliente entity."""


from datetime import date


class Cliente:
    """Class for manipulate Cliente data."""

    def __init__(self,
                 nome: str,
                 email: str,
                 data_nascimento: date,
                 profissao: str,
                 sexo: str) -> None:
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._profissao = profissao
        self._sexo = sexo

    @property
    def nome(self) -> str:
        """Get nome attribute."""
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Set new value to nome attribute."""
        self._nome = nome

    @property
    def email(self) -> str:
        """Get email attribute."""
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """Set new value to email attribute."""
        self._email = email

    @property
    def data_nascimento(self) -> date:
        """Get data_nascimento attribute."""
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        """Set new value to data_nascimento attribute."""
        self._data_nascimento = data_nascimento

    @property
    def profissao(self) -> str:
        """Get profissao attribute."""
        return self._profissao

    @profissao.setter
    def profissao(self, profissao: str) -> None:
        """Set new value to profissao attribute."""
        self._profissao = profissao

    @property
    def sexo(self) -> str:
        """Get sexo attribute."""
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str) -> None:
        """Set new value to sexo attribute."""
        self._sexo = sexo
