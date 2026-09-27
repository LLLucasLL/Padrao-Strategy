"""Estratégia de desconto para clientes Premium."""
from .desconto_strategy import DescontoStrategy


class DescontoPremium(DescontoStrategy):
    """Aplica 20% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.80
