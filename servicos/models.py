from django.db import models
from cadastro.models import Voluntario,Idoso

# Create your models here.


class ServicoSolicitado(models.Model):
    voluntario_id = models.ForeignKey(Voluntario, null=True, blank=True, on_delete=models.RESTRICT)
    idoso_id = models.ForeignKey(Idoso, on_delete=models.RESTRICT)
    servsolicitado = models.CharField(verbose_name='Serviço', max_length=30)
    tagservico = models.CharField(verbose_name='Etiqueta', max_length=15, choices=(
        (1, 'Serviços da Casa'),
        (2, 'Acompanhamento / Carona'),
        (3, 'Compras'),
        (4, 'Visita'),
        (5, 'Diversos')
    ))
    data_compromisso = models.DateField(verbose_name='Data', null=False, blank=False)
    hora_compromisso = models.TimeField(verbose_name='Horário', null=False, blank=False)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    observacao = models.TextField(verbose_name='Observação', blank=True, null=False)





