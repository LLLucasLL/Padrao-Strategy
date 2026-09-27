"""Testes de integração básica da API Flask."""
import pytest

from backend.app import app


@pytest.fixture
def client():
    """Cria um cliente de teste Flask sem iniciar o servidor real."""
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_calcular_vip(client):
    resposta = client.post("/api/calcular", json={"tipo": "VIP", "valor": 100})

    assert resposta.status_code == 200
    assert resposta.get_json()["valor_final"] == 90.0


def test_tipo_invalido(client):
    resposta = client.post("/api/calcular", json={"tipo": "DESCONHECIDO", "valor": 100})

    assert resposta.status_code == 404


def test_valor_negativo(client):
    resposta = client.post("/api/calcular", json={"tipo": "VIP", "valor": -10})

    assert resposta.status_code == 400
