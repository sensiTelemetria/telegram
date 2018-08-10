from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('novo-usuario/', views.novo_usuario, name='novo_usuario'),
    path('lista-usuarios/', views.usuarios, name='lista_usuarios'),
    path('deleta-usuario/<id>', views.deleta_usuario, name='deleta_usuario'),
]