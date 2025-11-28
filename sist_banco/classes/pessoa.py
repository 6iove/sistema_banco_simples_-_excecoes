# classe base 
class Pessoa:
    def __init__(self, id: str, cpf: str, nome: str):
        self._id = id
        self._cpf = cpf
        self._nome = nome

    @property
    def id(self):
        return self._id

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f"{self._nome} - CPF: {self._cpf}"