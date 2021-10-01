from django.urls import path
from . import views

urlpatterns =[
    path('solicitar/', views.solicitar_servico, name='solicitar'),
]