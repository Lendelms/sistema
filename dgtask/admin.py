from django.contrib import admin
from dgtask.models import *

class NivelUsuarioAdmin(admin.ModelAdmin):
	list_display = ['idnivelusuario','descricao','ativo']

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['idusuario','nome','cpf','datanascimento','idnivelusuario']

admin.site.register(NivelUsuario, NivelUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
