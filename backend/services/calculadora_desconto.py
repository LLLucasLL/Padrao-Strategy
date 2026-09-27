"""Contexto do padrão Strategy."""
from backend.strategies.desconto_strategy import DescontoStrategy


class CalculadoraDesconto:
    """Contexto que utiliza qualquer estratégia compatível com DescontoStrategy."""

    def __init__(self, strategy: DescontoStrategy):
        # A calculadora recebe uma estratégia por injeção de dependência.
        self.strategy = strategy

    def calcular(self, valor: float) -> float:
        """Delegamos o cálculo à estratégia atualmente selecionada."""
        return self.strategy.calcular(valor)
