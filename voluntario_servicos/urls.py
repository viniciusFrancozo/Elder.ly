from django.urls import path
from . import views

urlpatterns = [
    path('listar_servicos', views.listar_servicos, name='listar_servicos'),
    path('servico/<int:servico_id>', views.visualizar, name='visualizar')
]