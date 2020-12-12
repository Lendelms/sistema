from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from dgtask.models import *
#from dgtask.forms import FormularioVeiculo
from sistema.utilitarios import AuteticacaoObrigatoria


def index(request):
    return HttpResponse("Hello. You're at the polls index.")

class ListTask(AuteticacaoObrigatoria, ListView):
	"""docstring for List Tarefas"""
	# model = Chamado
	context_object_name = 'lista_tarefas'
	template_name = 'dgtask/list_task.html'
	def get_queryset(self):
		return Chamado.objects.all()
		
