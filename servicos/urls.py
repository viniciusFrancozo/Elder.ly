from django.urls import path
from . import views

urlpatterns =[
    path('solicitar/', views.solicitar_servico, name='solicitar'),
    path('meus_servicos/', views.meus_servicos, name='meus_servicos'),
    path('confirmar/<int:servico_id>', views.confirmar, name='confirmar')
]