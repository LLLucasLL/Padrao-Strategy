"""Contrato das estratégias de desconto."""
from abc import ABC, abstractmethod


class DescontoStrategy(ABC):
    """Define o comportamento que toda estratégia de desconto deve possuir."""

    @abstractmethod
    def calcular(self, valor: float) -> float:
        """Calcula o valor final da compra após aplicar o desconto."""
        raise NotImplementedError
