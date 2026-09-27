"""Ponto de entrada da aplicação Flask."""
from pathlib import Path
from flask import Flask, send_from_directory
from backend.controllers.desconto_controller import desconto_bp


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


app = Flask(
    __name__,
    # O Flask serve os arquivos da interface diretamente da pasta frontend.
    static_folder=str(FRONTEND_DIR),
    static_url_path="",
)

# Registra as rotas do controller.
app.register_blueprint(desconto_bp)


@app.get("/")
def index():
    """Entrega a página principal da aplicação."""
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/health")
def health():
    """Endpoint para verificar se o servidor está ativo."""
    return {"status": "ok"}


if __name__ == "__main__":
    # debug=True facilita o desenvolvimento local no VS Code.
    app.run(debug=True)