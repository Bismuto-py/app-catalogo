from django import forms
from .models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'tipo', 'ano', 'genero', 'descricao']

        labels = {
            'titulo': 'Título',
            'tipo': 'Tipo de obra',
            'ano': 'Ano de lançamento',
            'genero': 'Gênero do filme',
            'descricao': 'Descrição',
        }
