import os
import sys
import pytest

# Garante que o Python encontre o arquivo run.py na raiz do projeto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import app  # Importa o app do seu arquivo run.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_status_rota_inicial(client):
    """TESTE REAL: Valida se a aplicação responde na rota raiz (Status 200 ou 302)"""
    response = client.get('/')
    assert response.status_code in [200, 302]

def test_pagina_login_existe(client):
    """TESTE REAL: Verifica se o endpoint de login está estruturado no Flask"""
    response = client.get('/login')
    assert response.status_code in [200, 302]