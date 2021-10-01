from django.forms import ModelForm
from .models import ServicoSolicitado

class ServicoModel(ModelForm):
    class Meta:
        model = ServicoSolicitado
        fields = ('servsolicitado', 'tagservico', 'data_compromisso', 'hora_compromisso', 'observacao')
