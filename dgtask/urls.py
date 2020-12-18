from django.urls import path
from dgtask import views

urlpatterns = [path('',views.ListTask.as_view(), name='index'),
path('perfil_usuario/<int:pk>/', views.UsuarioSel.as_view(), name='sel-usuario'),
path('novo/',views.UsuarioNew.as_view(),name='novo-usuario'),
path('novo_chamado/',views.ChamadoNew.as_view(),name='novo-chamado')
#path('excluir/<int:pk>/', views.VeiculosDelete.as_view(), name='excluir-veiculo'),
#path('api/listar/', views.VeiculosListAPI.as_view(), name='api-listar-veiculo'),
]
