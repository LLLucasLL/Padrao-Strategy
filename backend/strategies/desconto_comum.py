"""Estratégia de desconto para clientes comuns."""
from .desconto_strategy import DescontoStrategy


class DescontoComum(DescontoStrategy):
    """Aplica 5% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.95
