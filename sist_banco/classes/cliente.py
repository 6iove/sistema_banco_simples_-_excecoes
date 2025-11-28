from .pessoa import Pessoa

# cliente herda pessoa 
class Cliente(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, email: str, data_nascimento: str = None):
        super().__init__(id, cpf, nome)
        self._email = email
        self._data_nascimento = data_nascimento
    
    @property
    def email(self):
        return self._email

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def __str__(self):
        return f"Cliente: {self._nome} | CPF: {self._cpf} | E-mail: {self._email}"
