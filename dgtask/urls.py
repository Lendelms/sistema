from django.urls import path
from dgtask import views

urlpatterns = [path('',views.index, name='index'),]
