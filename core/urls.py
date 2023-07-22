from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, atualizar, delete

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name= 'editar'),
    path('atualizar/<int:id>', atualizar, name= 'atualizar'),
    path('delete/<int:id>', delete, name='delete')
]