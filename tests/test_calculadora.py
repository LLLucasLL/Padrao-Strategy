"""Testes do contexto CalculadoraDesconto."""
import pytest

from backend.services.calculadora_desconto import CalculadoraDesconto
from backend.strategies.desconto_comum import DescontoComum
from backend.strategies.desconto_funcionario import DescontoFuncionario


def test_calculadora_usa_a_estrategia_recebida():
    """A calculadora deve delegar o cálculo para a estratégia injetada."""
    calculadora = CalculadoraDesconto(DescontoComum())

    assert calculadora.calcular(100) == pytest.approx(95)


def test_calculadora_permite_trocar_de_estrategia():
    """Estratégias diferentes podem ser usadas pelo mesmo contexto."""
    calculadora = CalculadoraDesconto(DescontoFuncionario())

    assert calculadora.calcular(1000) == pytest.approx(700)
