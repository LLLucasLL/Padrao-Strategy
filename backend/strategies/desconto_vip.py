"""Estratégia de desconto para clientes VIP."""
from .desconto_strategy import DescontoStrategy


class DescontoVIP(DescontoStrategy):
    """Aplica 10% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.90
