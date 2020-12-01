from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from veiculos.models import Veiculo
from django.urls import reverse_lazy
from veiculos.forms import FormularioVeiculo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class VeiculosList(ListView):
	"""view for VeiculosList"""
	# def get(self, request):
	# 	contexto = {
	# 		'lista_veiculos': Veiculo.objects.all().order_by('marca')
	# 	}
	# 	return render(request, 'veiculos/listar.html',contexto)
	model = Veiculo
	context_object_name = 'lista_veiculos'
	template_name = 'veiculos/listar.html'

class VeiculosNew(CreateView):
	"""Create for VeiculosNew"""
	model = Veiculo
	form_class = FormularioVeiculo
	template_name = 'veiculos/novo.html'
	success_url = reverse_lazy('listar-veiculos')

class VeiculosEdit(UpdateView):
	"""Update for VeiculosEdit"""
	model = Veiculo
	form_class = FormularioVeiculo
	template_name = 'veiculos/editar.html'
	success_url = reverse_lazy('listar-veiculos')

class VeiculosDelete(DeleteView):
	"""delete for Veiculos"""
	model = Veiculo
	template_name = 'veiculos/deletar.html'
	success_url = reverse_lazy('listar-veiculos')		
		