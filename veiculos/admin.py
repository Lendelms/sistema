from django.contrib import admin
from veiculos.models import *

# Register your models here.

class VeiculoAdmin(admin.ModelAdmin):
	"""Veiculos Admin"""
	list_display = ['marca','modelo','ano_fabricacao','modelo_fabricacao','combustivel']
	search_fields = ['marca','modelo']
	list_filter = ['combustivel']

admin.site.register(Veiculo, VeiculoAdmin)
		