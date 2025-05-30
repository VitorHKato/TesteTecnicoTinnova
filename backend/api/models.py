"""
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
        Classe com informações sobre o veículo.
"""
from django.core.exceptions import ValidationError
from django.db import models


MARCAS_VALIDAS = ['Volkswagen', 'Ford', 'Honda', 'Chevrolet', 'Toyota',
                 'Nissan', 'Fiat', 'Hyundai', 'Kia', 'Peugeot',
                 'Citroën', 'Renault', 'Mitsubishi', 'Subaru',
                 'Mazda', 'Suzuki', 'Dodge', 'Chrysler',
                 'Jeep', 'Land Rover', 'Volvo', 'Audi',
                 'BMW', 'Mercedes-Benz', 'Porsche']


class Veiculo(models.Model):
    """
        Classe com informações sobre o veículo.
        :param
            nome: Nome do veículo.
            marca: Marca do veículo.
            ano: Ano do veículo.
            descricao: Descrição do veículo.
            vendido: Indica se o veículo foi vendido.
            created: Data de criação do registro.
            updated: Data de atualização do registro.
    """
    nome = models.CharField(max_length=100, verbose_name="Nome do Veículo")
    marca = models.CharField(max_length=100, verbose_name="Marca do Veículo")
    ano = models.IntegerField(verbose_name="Ano do Veículo")
    descricao = models.TextField(verbose_name="Descrição do Veículo")
    vendido = models.BooleanField(default=False, verbose_name="Vendido?")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")


    def __str__(self):
        return self.nome


    @staticmethod
    def valida_marcas(value):
        """
            Valida nome de marcas de veículos.
            :param value:
            :raises: ValidationError se a marca não for válida.
        """
        if value not in MARCAS_VALIDAS:
            raise ValidationError(
                f"Marca '{value}' não é válida. Marcas válidas: {', '.join(MARCAS_VALIDAS)}")
