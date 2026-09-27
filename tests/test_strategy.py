"""Testes unitários das estratégias de desconto."""
import pytest

from backend.strategies.desconto_aniversario import DescontoAniversario
from backend.strategies.desconto_comum import DescontoComum
from backend.strategies.desconto_funcionario import DescontoFuncionario
from backend.strategies.desconto_premium import DescontoPremium
from backend.strategies.desconto_promocional import DescontoPromocional
from backend.strategies.desconto_vip import DescontoVIP


@pytest.mark.parametrize(
    "estrategia, esperado",
    [
        (DescontoComum(), 95.0),
        (DescontoVIP(), 90.0),
        (DescontoPremium(), 80.0),
        (DescontoAniversario(), 85.0),
        (DescontoPromocional(), 75.0),
        (DescontoFuncionario(), 70.0),
    ],
)
def test_descontos_para_100_reais(estrategia, esperado):
    """Todas as regras devem produzir o resultado definido no laboratório."""
    assert estrategia.calcular(100.0) == pytest.approx(esperado)


@pytest.mark.parametrize("valor", [500.0, 1000.0, 2500.0])
def test_estrategia_vip_para_outros_valores(valor):
    """O cálculo deve continuar correto para diferentes valores de compra."""
    assert DescontoVIP().calcular(valor) == pytest.approx(valor * 0.90)
