from django.db import models
from cadastro.models import Voluntario, Idoso
# from taggit.managers import TaggableManager


# Create your models here.


class ServicoSolicitado(models.Model):
    voluntario_id = models.ForeignKey(Voluntario, null=True, blank=True, on_delete=models.RESTRICT)
    idoso_id = models.ForeignKey(Idoso, on_delete=models.RESTRICT, blank=True)
    servsolicitado = models.CharField(verbose_name='Serviço', max_length=30)
    # tagservico = TaggableManager()
    tagservico = models.CharField(verbose_name='Etiqueta', max_length=15, choices=(
        ('', 'Escolha uma Etiqueta'),
        ('1', 'Serviços da Casa'),
        ('2', 'Acompanhamento / Carona'),
        ('3', 'Compras'),
        ('4', 'Visita'),
        ('5', 'Diversos')
    ), default='')
    data_compromisso = models.DateField(verbose_name='Data', null=False, blank=False)
    hora_compromisso = models.TimeField(verbose_name='Horário', null=False, blank=False)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    observacao = models.TextField(verbose_name='Observação', blank=True, null=False)





