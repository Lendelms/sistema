from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from dgtask.models import *
from dgtask.forms import *
from sistema.utilitarios import AuteticacaoObrigatoria
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello. You're at the task index.")

class ListTask(AuteticacaoObrigatoria, ListView):
	"""docstring for List Tarefas"""
	model = Usuario
	context_object_name = {'usuario', }
	template_name = 'dgtask/list_task.html'
	def get_queryset(self):
		return Usuario.objects.values().all()

class UsuarioSel(AuteticacaoObrigatoria, View):
	"""class baseada para verificar usuarios novos ou já cadastrados"""
	def get(self, request, pk):
		usu = Usuario.objects.values().filter(idusuario=pk)
		nivelusu = NivelUsuario.objects.values().all()
		data = {
			'usuario': usu,
			'nivelusuario': nivelusu
		}
		if usu.count() > 0:
			return render(request, 'dgtask/perfil_usuario.html', data)
		else:
			return render(request, 'dgtask/novo_user.html')


class UsuarioEdit(AuteticacaoObrigatoria, UpdateView):
	"""Create for VeiculosNew"""
	model = Usuario
	form_class = FormularioUsuario
	template_name = 'dgtask/perfil_usuario.html'
	success_url = reverse_lazy('index')
	#def get_object(self, queryset=None):
		#chave = self.kwargs.get("pk")
		#usu = Usuario.objects.filter(idusuario=chave)	
		#if usu.count() > 0:
			#return render(self, 'dgtask/perfil_usuario.html', usu)
		#else:
			#return render(self, 'dgtask/novo_user.html')
			#template_name = 'dgtask/novo_user.html'
			#success_url = reverse_lazy('index')
	# def get_queryset(request):
		# usuario = get_object_or_404(Usuario, pk=request.iduser)
		# return render(request, 'dgtask/perfil_usuario.html', {'usuario': usuario})

class UsuarioNew(AuteticacaoObrigatoria, CreateView):
	"""Create for VeiculosNew"""
	model = Usuario
	form_class = FormularioUsuario
	template_name = 'dgtask/novo_user.html'
	success_url = reverse_lazy('index')

class ChamadoNew(AuteticacaoObrigatoria, CreateView):
	"""Create for VeiculosNew"""
	model = Chamado
	form_class = FormularioChamado
	template_name = 'dgtask/novo_chamado.html'
	success_url = reverse_lazy('index')
	# usu = Usuario.objects.values().filter(idusuario=pk)
	#context_object_name =