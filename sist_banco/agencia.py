from typing import List
from classes.conta import Conta
from classes.funcionario import Funcionario
from exceptions import ContaNaoEncontradaError

class Agencia:
    def __init__(self, numero: int, endereco: str, fone: str, funcionario: Funcionario):
        self._numero = numero
        self._endereco = endereco
        self._fone = fone
        self._funcionario = funcionario 
        self._contas: List[Conta] = []

    def adicionar_conta(self, conta: Conta):
        # joga conta pra dentro da lista
        self._contas.append(conta)

    def buscar_conta(self, numero: str) -> Conta:
        # procura conta pelo número
        for c in self._contas:
            if c.numero == numero:
                return c
        raise ContaNaoEncontradaError(f"Conta {numero} não encontrada na agência.")
