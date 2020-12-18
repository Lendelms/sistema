from django import forms
from dgtask.models import *

class FormularioUsuario(forms.ModelForm):
    """
    	Formulario para o model Usuario
    """
    class Meta:
    	model = Usuario
    	exclude = []

class FormularioChamado(forms.ModelForm):
    """
    	Formulario para o model Chamado
    """
    class Meta:
    	model = Chamado
    	exclude = ['lido', 'idusuariocriou','ativo']