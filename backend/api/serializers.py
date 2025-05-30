"""
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
        Serializer das classes da api.
"""

from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(validators=[Veiculo.valida_marcas])
    """
    Serializer da classe Veiculo. Converte instâncias do modelo Veiculo para JSON e vice-versa.
    """

    class Meta:
        model = Veiculo
        fields = '__all__'  # Include all fields from the Veiculo model
