from django.contrib.auth.mixins import LoginRequiredMixin

class AuteticacaoObrigatoria(LoginRequiredMixin):
	"""class for AuteticacaoObrigatoria"""
	login_url = '/'
