import pytest

from app import app
from unittest import TestCase


class MyTestCase(TestCase):
    def setUp(self):
        # Configuração inicial para cada teste
        app.testing = True
        self.client = app.test_client()

    def test_home_route(self):
        # Teste para a rota '/'
        response = self.client.get('/')
        assert response.status_code == 200
        assert response.data == b'<h1>Hello from Flask & Docker</h1>'
