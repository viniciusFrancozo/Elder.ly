from django import forms
from .models import ServicoSolicitado, Idoso


class ServicoModel(forms.ModelForm):
    class Meta:
        model = ServicoSolicitado
        fields = ('idoso_id', 'servsolicitado', 'tagservico', 'data_compromisso', 'hora_compromisso', 'observacao')
        labels = {
            'servsolicitado': '',
            'tagservico': '',
            'data_compromisso': '',
            'hora_compromisso': '',
            'observacao': ''
        }
        widgets = {
            'idoso_id': forms.HiddenInput(),
            'servsolicitado': forms.TextInput(attrs={'placeholder': 'Serviço'}),
            'data_compromisso': forms.TextInput(attrs={'placeholder': 'Data'}),
            'hora_compromisso': forms.TextInput(attrs={'placeholder': 'Horário'}),
            'observacao': forms.Textarea(attrs={'placeholder': 'Observação'}),
            # 'tagservico': forms.ChoiceField(attrs={'placeholder': 'Serviço'}),
        }
