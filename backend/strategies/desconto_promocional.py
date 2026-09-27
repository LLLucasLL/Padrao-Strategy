"""Estratégia de desconto promocional."""
from .desconto_strategy import DescontoStrategy


class DescontoPromocional(DescontoStrategy):
    """Aplica 25% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.75
