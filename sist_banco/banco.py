# banco.py
from typing import List
from agencia import Agencia

# lista de agencias 
class Banco:
    def __init__(self, cnpj: str, nome: str):
        self._cnpj = cnpj
        self._nome = nome
        self._agencias: List[Agencia] = []

    # adiciona agencia na lista
    def adicionar_agencia(self, agencia: Agencia):
        self._agencias.append(agencia)

    def listar_agencias(self):
        return list(self._agencias)
