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
