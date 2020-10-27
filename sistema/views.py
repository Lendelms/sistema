from django.views.generic import View
from django.shortcuts import render

class Autenticacao(View):
	"""class baseada para Autenticacao usuarios"""
	def get(self, request):
		contexto = {
			'usuario':'Usuário',
			'senha':'Senha'
		}
		return render(request, 'autenticacao2.html', contexto)
