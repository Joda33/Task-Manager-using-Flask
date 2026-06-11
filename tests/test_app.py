import pytest
# Importa o objeto 'app' do seu projeto. 
# Nota: Se o seu arquivo principal tiver outro nome, ajuste 'todo_project' para o nome correto.
from todo_project import app 
@pytest.fixture
def client():
    """Configura o cliente de teste do Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Teste Funcional: Verifica se a página inicial carrega com sucesso (Status 200)"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page_loads(client):
    """Verifica se a rota de login está acessível"""
    response = client.get('/login')
    assert response.status_code == 200

def test_about_page_content(client):
    """Verifica se uma string específica aparece na página 'Sobre'"""
    response = client.get('/about')
    assert b"Aditya Bagad" in response.data