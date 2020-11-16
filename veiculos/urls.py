from django.urls import path
from veiculos import views

urlpatterns = [path('',views.VeiculosList.as_view(),name='lista-veiculos')]
