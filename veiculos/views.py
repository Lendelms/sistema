from django.shortcuts import render
from django.views.generic import View, ListView, CreateView
from veiculos.models import Veiculo

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