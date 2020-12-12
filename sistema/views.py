from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

class Autenticacao(View):
	"""class baseada para Autenticacao usuarios"""
	def get(self, request):
		contexto = {
			'usuario':'Usuário',
			'senha':'Senha',
			'mostraerr':'invisible'
		}
		return render(request, 'autenticacao2.html', contexto)
		# return render(request, 'autenticacao.html', contexto)

	def post(self,request):
		#armazena valores requisicao
		usuario = request.POST.get('usuario',None)
		senha = request.POST.get('senha',None)

		#log no terminal
		#logger.info('Usuario: {usuario}'.format(usuario=usuario))
		#logger.info('Senha: {senha}'.format(senha=senha))

		#autenticacao
		user = authenticate(request, username=usuario, password=senha)
		if user is not None:

			#verifica se usuario esta ativo
			if user.is_active:
				login(request, user)
				return render(request, 'base/basedgtask.html', {'mensagem':'Usuario Bem vindo'})
				# return HttpResponse('Usuario Autenticado com sucesso')

			return render(request, 'autenticacao2.html', {'mensagem':'Usuario inativo', 'mostraerr':'visible'})

		return render(request, 'autenticacao2.html', {'mensagem':'Usuario ou senha incorreto','mostraerr':'visible'})

		#return HttpResponse('Em Desenvolvimento')
