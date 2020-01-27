from django import forms
from gato.models import Gato

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = [
            'nome',
            'raca',
            'cor',
            'idade',
        ] 