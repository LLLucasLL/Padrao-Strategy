"""Estratégia de desconto para funcionários."""
from .desconto_strategy import DescontoStrategy


class DescontoFuncionario(DescontoStrategy):
    """Aplica 30% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.70
