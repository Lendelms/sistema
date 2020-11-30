from django.urls import path
from veiculos import views

urlpatterns = [path('',views.VeiculosList.as_view(),name='lista-veiculos'),
path('novo/',views.VeiculosNew.as_view(),name='novo-veiculo'),
path('<int:pk>/', views.VeiculosEdit.as_view(), name='editar-veiculo'),
path('excluir/<int:pk>/', views.VeiculosDelete.as_view(), name='excluir-veiculo')]
