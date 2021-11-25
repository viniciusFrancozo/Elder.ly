from django.urls import path
from . import views

urlpatterns =[
    path('solicitar/', views.solicitar_servico, name='solicitar'),
    path('meus_servicos/', views.meus_servicos, name='meus_servicos'),
    path('meus_servicos/voluntario', views.meus_servicos_voluntario, name='meus_servicos_voluntario'),
    path('iniciar/<int:servico_id>', views.iniciar, name='iniciar'),
    path('confirmar/<int:servico_id>', views.confirmar, name='confirmar'),
    path('encerrar/<int:servico_id>', views.encerrar, name='encerrar')
]