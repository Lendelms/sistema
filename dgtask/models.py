from django.db import models

class NivelUsuario(models.Model):
	"""Nivel Usuario"""
	idnivelusuario = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=100)
	ativo = models.BooleanField(default=True)
	def __str__(self):
		return '{0} - {1}'.format(self.idnivelusuario, self.descricao)


class Usuario(models.Model):
	"""DGtask for Usuario"""
	idusuario = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14,unique=True)
	datanascimento = models.DateField()
	sexo = models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1, blank=True)
	email = models.CharField(max_length=100)
	telefone = models.CharField(max_length=12)
	endereco = models.CharField(max_length=100)
	idnivelusuario = models.ForeignKey(NivelUsuario, on_delete=models.CASCADE)
	def __str__(self):
		return '{0} - {1}'.format(self.idusuario, self.nome)

class SistemaCidadeSuporte(models.Model):
	"""DGtask for SistemaCidadeSuporte"""
	idsistemacidadesuporte = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	link = models.CharField(max_length=50)
	servidor = models.CharField(max_length=50)
	ipservidor = models.CharField(max_length=20)
	def __str__(self):
		return '{0} - {1}'.format(self.idsistemacidadesuporte, self.nome)

class PrioridadeChamado(models.Model):
	"""docstring for Prioridade chamado"""
	idprioridadechamado = models.AutoField(primary_key=True)
	descprioridade = models.CharField(max_length=20)
	tempo = models.IntegerField()
	ativo = models.BooleanField(default=True)
	def __str__(self):
		return '{0} - {1}'.format(self.idprioridadechamado, self.descprioridade)

class SituacaoChamado(models.Model):
	"""docstring for Situacao Chamado"""
	idsituacaochamado = models.AutoField(primary_key=True)
	descsituacao = models.CharField(max_length=20)
	ativo = models.BooleanField(default=True)
	def __str__(self):
		return '{0} - {1}'.format(self.idsituacaochamado, self.descsituacao)
		
class MensagemChamado(models.Model):
	"""docstring for Mensagem Chamado"""
	idmensagemchamado = models.AutoField(primary_key=True)
	idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	mensagem = models.CharField(max_length=100)
	idusuariocriou = models.IntegerField()
	dataregistro = models.DateField(auto_now=True)
	lido = models.BooleanField(default=False)
	def __str__(self):
		return '{0} - {1}'.format(self.idmensagemchamado, self.mensagem)

class Chamado(models.Model):
	"""docstring for Chamado"""
	idchamado = models.AutoField(primary_key=True)
	idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
	idprioridadechamado = models.ForeignKey(PrioridadeChamado, on_delete=models.CASCADE)
	idsistemacidadesuporte = models.ForeignKey(SistemaCidadeSuporte, on_delete=models.CASCADE)
	idsituacaochamado = models.ForeignKey(SituacaoChamado, on_delete=models.CASCADE)
	mensagem = models.CharField(max_length=250,null=True)
	data = models.DateField(null=True)
	comentario = models.CharField(max_length=100)
	lido = models.BooleanField(default=False)
	idusuariocriou = models.IntegerField(null=True)
	dataregistro = models.DateField(auto_now=True)
	ativo = models.BooleanField(default=True)

	# idmensagemchamado = models.ForeignKey(MensagemChamado, on_delete=models.CASCADE)
