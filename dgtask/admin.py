from django.contrib import admin
from dgtask.models import *

class NivelUsuarioAdmin(admin.ModelAdmin):
	list_display = ['idnivelusuario','descricao','ativo']

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['idusuario','nome','cpf','datanascimento','idnivelusuario']

class SistemaCidadeSuporteAdmin(admin.ModelAdmin):
	list_display = ['idsistemacidadesuporte', 'nome', 'link', 'servidor', 'ipservidor']

class PrioridadeChamadoAdmin(admin.ModelAdmin):
	list_display = ['idprioridadechamado', 'descprioridade', 'tempo', 'ativo']

class SituacaoChamadoAdmin(admin.ModelAdmin):
	list_display = ['idsituacaochamado', 'descsituacao', 'ativo']

class MensagemChamadoAdmin(admin.ModelAdmin):
	list_display = ['idmensagemchamado', 'idusuario', 'mensagem', 'idusuariocriou', 'dataregistro',	'lido']

class ChamadoAdmin(admin.ModelAdmin):
	list_display = ['idchamado', 'idusuario', 'idprioridadechamado', 'idsistemacidadesuporte', 'mensagem', 'data', 'idsituacaochamado', 'comentario', 'ativo']

admin.site.register(NivelUsuario, NivelUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(SistemaCidadeSuporte, SistemaCidadeSuporteAdmin)
admin.site.register(PrioridadeChamado, PrioridadeChamadoAdmin)
admin.site.register(SituacaoChamado, SituacaoChamadoAdmin)
admin.site.register(MensagemChamado, MensagemChamadoAdmin)
admin.site.register(Chamado, ChamadoAdmin)
