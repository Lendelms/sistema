from django import forms
from veiculos.models import Veiculo

class FormularioVeiculo(forms.ModelForm):
    """
    	Formulario para o model Veiculo
    """
    class Meta:
    	model = Veiculo
    	exclude = []