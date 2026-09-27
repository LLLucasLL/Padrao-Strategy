"""Middleware responsável por validar dados recebidos pela API."""
from functools import wraps
from flask import jsonify, request


def validar_calculo(func):
    """Valida o corpo JSON antes de permitir que o controller execute."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        dados = request.get_json(silent=True)

        if not isinstance(dados, dict):
            return jsonify({"erro": "O corpo da requisição deve ser um JSON."}), 400

        if not dados.get("tipo"):
            return jsonify({"erro": "O campo 'tipo' é obrigatório."}), 400

        if "valor" not in dados:
            return jsonify({"erro": "O campo 'valor' é obrigatório."}), 400

        try:
            valor = float(dados["valor"])
        except (TypeError, ValueError):
            return jsonify({"erro": "O campo 'valor' deve ser numérico."}), 400

        if valor < 0:
            return jsonify({"erro": "O valor da compra não pode ser negativo."}), 400

        # Armazena o valor já convertido para o controller usar diretamente.
        dados["valor"] = valor
        return func(*args, **kwargs)

    return wrapper
