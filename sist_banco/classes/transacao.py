from datetime import datetime
from .cliente import Cliente


class Transacao:
    def __init__(self, tipo: str, valor: float, saldo: float, cliente: Cliente):
        self._tipo = tipo
        self._valor = valor
        self._saldo = saldo
        self._data = datetime.now()
        self._cliente = cliente
        

    def __str__(self):
        return f"{self._data} | {self._tipo:<10} | R$ {self._valor:8.2f} | Saldo: R$ {self._saldo:8.2f} | Cliente: {self._cliente}"
