"""
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
        Realiza testes unitários da api.
"""

from django.utils import timezone
from django.test import TestCase
from .models import Veiculo
from rest_framework.test import APIClient
from rest_framework import status


class VeiculoTests(TestCase):
    """
        Testes unitários para o modelo Veiculo.
    """
    def setUp(self):
        """
            Faz a configuração inicial.
        """
        self.client = APIClient()
        self.veiculo_data = {
            "marca": "Ford",
            "nome": "Fiesta",
            "ano": 2012,
            "descricao": "Veículo compacto",
            "created": timezone.now(),
            "updated": timezone.now(),
            "vendido": False
        }
        self.veiculo = Veiculo.objects.create(**self.veiculo_data)


    def test_listar_veiculos(self):
        """
            Testa o endpoint /api/veiculos/ (GET).
        """
        response = self.client.get("/api/veiculos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_nao_vendidos(self):
        """
            Testa o endpoint "/api/veiculos/nao_vendidos"
        """
        response = self.client.get("/api/veiculos/nao_vendidos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_por_decada(self):
        """
            Testa o endpoint "/api/veiculos/por_decada"
        """
        response = self.client.get("/api/veiculos/por_decada/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_filtrar_por_marca(self):
        """
            Testa o filtro de veículos por marca "/api/veiculos/?termo=Ford (GET).
        """
        response = self.client.get("/api/veiculos/?termo=Ford")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


    def test_criar_veiculo_valido(self):
        """
            Testa o endpoint "/api/veiculos/ (POST)"
        """
        response = self.client.post("/api/veiculos/", self.veiculo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_ultima_semana(self):
        """
            Testa o endpoint "/api/veiculos/ultima_semana (GET)"
        """
        response = self.client.get("/api/veiculos/ultima_semana")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_criar_veiculo_marca_invalida(self):
        """
            Testa a criação de um veículo com marca inválida.
            Deve retornar erro 400.
        """
        invalido = {
            "marca": "Ferrari",
            "modelo": "F8",
            "ano_fabricacao": 2022,
            "vendido": False
        }
        response = self.client.post("/api/veiculos/", invalido, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("marca", response.data)