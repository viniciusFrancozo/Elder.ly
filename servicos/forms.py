from django import forms
from .models import ServicoSolicitado, Idoso


class ServicoModel(forms.ModelForm):
    class Meta:
        model = ServicoSolicitado
        fields = ('idoso_id', 'servsolicitado', 'tagservico', 'data_compromisso', 'hora_compromisso', 'observacao')
        widgets = {
            'idoso_id': forms.HiddenInput()
        }
