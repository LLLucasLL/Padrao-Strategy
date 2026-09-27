"""Estratégia de desconto para clientes aniversariantes."""
from .desconto_strategy import DescontoStrategy


class DescontoAniversario(DescontoStrategy):
    """Aplica 15% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.85
