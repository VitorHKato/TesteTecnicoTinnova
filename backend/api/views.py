"""
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
        Views da API.
"""
import datetime
from django.db.models import Q
from rest_framework import viewsets
from .models import Veiculo
from .serializers import VeiculoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer

    def get_queryset(self):
        """
            Retorna todos os veículos, filtrando por termo de pesquisa se fornecido.
            :param
                nome: Nome do veículo.
                marca: Marca do veículo.
                ano: Ano do veículo.
            :return
                queryset: Queryset de veículos filtrados.
        """
        queryset = Veiculo.objects.all()
        termo = self.request.query_params.get('termo', None)
        if termo:
            queryset = queryset.filter(Q(nome__icontains=termo) |
                                       Q(marca__icontains=termo) |
                                       Q(ano__icontains=termo))
        return queryset


    @action(detail=False, methods=['get'])
    def nao_vendidos(self, request):
        """
            Retorna todos os veículos que não foram vendidos.
            :return
                Response: Lista de veículos não vendidos.
        """
        total = Veiculo.objects.filter(vendido=False).count()
        return Response({"nao_vendidos": total}, status=200)


    @action(detail=False, methods=['get'])
    def por_decada(self, request):
        """
            Retorna a quantidade de veículos por década.
            :return
                Response: Dicionário com a quantidade de veículos por década.
        """
        veiculos = Veiculo.objects.all()
        distribuicao = {}
        for v in veiculos:
            decada = (v.ano // 10) * 10
            key = f"Década {decada}"
            distribuicao[key] = distribuicao.get(key, 0) + 1
        return Response(distribuicao)


    @action(detail=False, methods=['get'])
    def por_fabricante(self, request):
        """
            Retorna a quantidade de veículos por fabricante.
            :return
                Response: Dicionário com a quantidade de veículos por fabricante.
        """
        veiculos = Veiculo.objects.all()
        distribuicao = {}
        for v in veiculos:
            key = v.marca
            distribuicao[key] = distribuicao.get(key, 0) + 1
        return Response(distribuicao)


    @action(detail=False, methods=['get'])
    def ultima_semana(self, request):
        """
            Retorna todos os veículos criados na última semana.
            :return
                Response: Lista de veículos criados na última semana.
        """
        veiculos = Veiculo.objects.filter(created__gte=datetime.datetime.now() - datetime.timedelta(days=7))
        serializer = self.get_serializer(veiculos, many=True)
        return Response(serializer.data)