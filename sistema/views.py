from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from dgtask.models import *
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
				usu = Usuario.objects.values().filter(idusuario=user.id)
				# request.session['attusuario'] = usu
				data = { 'usuario': usu }
				return render(request, 'dgtask/list_task.html', data)
				# return HttpResponse('Usuario Autenticado com sucesso')

			return render(request, 'autenticacao2.html', {'mensagem':'Usuario inativo', 'mostraerr':'visible','usuario':'Usuário', 'senha':'Senha'})

		return render(request, 'autenticacao2.html', {'mensagem':'Usuario ou senha incorreto','mostraerr':'visible','usuario':'Usuário', 'senha':'Senha'})

		#return HttpResponse('Em Desenvolvimento')
