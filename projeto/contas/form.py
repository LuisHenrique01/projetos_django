from django.forms import ModelForm
from .models import Transacoa

class TransacoaForms(ModelForm):
    class Meta:
        model = Transacoa
        fields = ['data', 'descricao', 'valor', 'categoria', 'observacao']