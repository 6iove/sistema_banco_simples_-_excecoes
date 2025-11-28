from .pessoa import Pessoa

# herda de pessoa 
class Funcionario(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, matricula: str):
        super().__init__(id, cpf, nome)
        self._matricula = matricula

    @property
    def matricula(self):
        return self._matricula

    def __str__(self):
        return f"Funcionario: {self._nome} | Matrícula: {self._matricula}"
