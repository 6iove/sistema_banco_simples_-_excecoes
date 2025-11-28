from datetime import datetime
from .conta import Conta

class Emprestimo:
    def __init__(self, valor: float, taxa_juros: float, prazo_meses: int, conta: Conta):
        if valor <= 0:
            raise ValueError("Valor do empréstimo deve ser > 0")
        if prazo_meses <= 0:
            raise ValueError("Prazo deve ser maior que 0 meses")
        self._valor = float(valor)
        self._taxa_juros = float(taxa_juros)
        self._prazo_meses = int(prazo_meses)
        self._conta = conta
        self._data_contratacao = datetime.now()
        self._valor_parcela = self.calcular_parcela()

    def calcular_parcela(self):
        # juros aplicado
        montante = self.valor * (1 + self.taxa_juros)
        return montante / self.prazo_meses
