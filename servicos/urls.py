from django.urls import path
from . import views

urlpatterns =[
    path('', views.solicitar_servico, name='solicitar')
]