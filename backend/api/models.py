from django.db import models

class Veiculo(models.Model):
    """
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
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
