from django.forms import ModelForm

from cadastroApi.models import FeriadoModel


class FeriadoForm(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome', 'data']
