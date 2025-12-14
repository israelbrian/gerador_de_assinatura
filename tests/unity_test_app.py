import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Cria e configura uma nova instância do app para cada teste."""
    yield flask_app

@pytest.fixture
def client(app):
    """Um cliente de teste para o app."""
    return app.test_client()

def test_form_page_loads(client):
    """
    Testa se a página principal (que contém o formulário) carrega com sucesso.
    """
    response = client.get('/')
    assert response.status_code == 200
    # Verifique se um texto esperado está na página
    assert b"gerador de assinatura" in response.data.lower()
