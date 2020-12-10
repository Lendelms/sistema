from django.contrib import admin
from dgtask.models import *

class NivelUsuarioAdmin(admin.ModelAdmin):
	list_display = ['idnivelusuario','descricao','ativo']


admin.site.register(NivelUsuario, NivelUsuarioAdmin)
