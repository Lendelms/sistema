from django import forms
from dgtask.models import *

class FormularioUsuario(forms.ModelForm):
    """
    	Formulario para o model Usuario
    """
    class Meta:
    	model = Usuario
    	exclude = []