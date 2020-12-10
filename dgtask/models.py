from django.db import models

class NivelUsuario(models.Model):
	"""Nivel Usuario"""
	idnivelusuario = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=100)
	ativo = models.BooleanField(default=True)


class Usuario(models.Model):
	"""DGtask for Usuario"""
	idusuario = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14,unique=True)
	datanascimento = models.DateField()
	password = models.CharField(max_length=80)
	email = models.CharField(max_length=100)
	telefone = models.CharField(max_length=12)
	endereco = models.CharField(max_length=100)
	idnivelusuario = models.ForeignKey(NivelUsuario, on_delete=models.CASCADE)

class SistemaCidadeSuporte(models.Model):
	"""DGtask for SistemaCidadeSuporte"""
	idsistemacidadesuporte = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	link = models.CharField(max_length=50)
	servidor = models.CharField(max_length=50)
	ipservidor = models.CharField(max_length=20)

class PrioridadeChamado(models.Model):
	"""docstring for Prioridade chamado"""
	idprioridadechamado = models.AutoField(primary_key=True)
	descprioridade = models.CharField(max_length=20)
	tempo = models.IntegerField()
	ativo = models.BooleanField(default=True)

class SituacaoChamado(models.Model):
	"""docstring for Situacao Chamado"""
	idsituacaochamado = models.AutoField(primary_key=True)
	descsituacao = models.CharField(max_length=20)
	ativo = models.BooleanField(default=True)
		
class MensagemChamado(models.Model):
	"""docstring for Mensagem Chamado"""
	idmensagemchamado = models.AutoField(primary_key=True)
	idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	mensagem = models.CharField(max_length=100)
	data = models.DateField()
	idusuariocriou = models.IntegerField()
	dataregistro = models.DateField(auto_now=True)
	lido = models.BooleanField(default=False)

class Chamado(models.Model):
	"""docstring for Chamado"""
	idchamado = models.AutoField(primary_key=True)
	idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	idprioridadechamado = models.ForeignKey(PrioridadeChamado, on_delete=models.CASCADE)
	idsistemacidadesuporte = models.ForeignKey(SistemaCidadeSuporte, on_delete=models.CASCADE)
	idmensagemchamado = models.ForeignKey(MensagemChamado, on_delete=models.CASCADE)
	idsituacaochamado = models.ForeignKey(SituacaoChamado, on_delete=models.CASCADE)
	comentario = models.CharField(max_length=100)
	ativo = models.BooleanField(default=True)

