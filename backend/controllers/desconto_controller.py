"""Controller HTTP responsável pelos cálculos de desconto."""
from flask import Blueprint, jsonify, request

from backend.middleware.validacao import validar_calculo
from backend.services.calculadora_desconto import CalculadoraDesconto
from backend.strategies.desconto_aniversario import DescontoAniversario
from backend.strategies.desconto_comum import DescontoComum
from backend.strategies.desconto_funcionario import DescontoFuncionario
from backend.strategies.desconto_premium import DescontoPremium
from backend.strategies.desconto_promocional import DescontoPromocional
from backend.strategies.desconto_vip import DescontoVIP


desconto_bp = Blueprint("desconto", __name__, url_prefix="/api")

# O controller conhece as classes disponíveis para expor a seleção à API.
# A CalculadoraDesconto, que é o contexto do Strategy, continua desacoplada delas.
ESTRATEGIAS = {
    "COMUM": DescontoComum,
    "VIP": DescontoVIP,
    "PREMIUM": DescontoPremium,
    "ANIVERSARIO": DescontoAniversario,
    "PROMOCIONAL": DescontoPromocional,
    "FUNCIONARIO": DescontoFuncionario,
}


@desconto_bp.get("/estrategias")
def listar_estrategias():
    """Retorna as estratégias disponíveis para a interface."""
    return jsonify({"estrategias": list(ESTRATEGIAS.keys())})


@desconto_bp.post("/calcular")
@validar_calculo
def calcular_desconto():
    """Seleciona a estratégia e devolve o valor final da compra."""
    dados = request.get_json()
    tipo = str(dados["tipo"]).strip().upper()
    valor = dados["valor"]

    estrategia_cls = ESTRATEGIAS.get(tipo)
    if estrategia_cls is None:
        return jsonify({"erro": f"Estratégia '{tipo}' não encontrada."}), 404

    # O contexto recebe a estratégia sem precisar conhecer sua implementação.
    calculadora = CalculadoraDesconto(estrategia_cls())
    resultado = calculadora.calcular(valor)

    return jsonify({
        "tipo": tipo,
        "valor_original": valor,
        "valor_final": round(resultado, 2),
    })
