"""
        Desenvolvedor: Vitor Henrique Kato
        Data: 30/05/2025
        Rotas da api.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VeiculoViewSet

router = DefaultRouter()
router.register(r'veiculos', VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('', include(router.urls)),
]