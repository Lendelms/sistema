from rest_framework import serializers
from veiculos.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
	"""Serializador for model Veiculo"""
	class Meta:
		model = Veiculo
		exclude = []
		#fields = []

		