from django.urls import path
from dgtask import views

urlpatterns = [path('',views.ListTask.as_view(), name='index'),
#path('novo/',views.VeiculosNew.as_view(),name='novo-veiculo'),
#path('<int:pk>/', views.VeiculosEdit.as_view(), name='editar-veiculo'),
#path('excluir/<int:pk>/', views.VeiculosDelete.as_view(), name='excluir-veiculo'),
#path('api/listar/', views.VeiculosListAPI.as_view(), name='api-listar-veiculo'),
]
