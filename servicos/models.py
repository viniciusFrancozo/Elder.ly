from django.db import models
from cadastro.models import Voluntario,Idoso

# Create your models here.

class ServicoSolicitado(models.Model):
    voluntario_id = models.ForeignKey(Voluntario, null=True, blank=True, on_delete=models.RESTRICT)
    idoso_id = models.ForeignKey(Idoso, on_delete=models.RESTRICT)
    servsolicitado = models.CharField(max_length=30)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    observacao = models.TextField(blank=True, null=False)

class Servicos(models.Model):
    servico = models.CharField(choices=(
        (1, 'Serviços da Casa'),
        (2, 'Acompanhamento'),
        
    ))





