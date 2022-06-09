from django.urls import path
from .views import listarLivros, inserirLivro

urlpatterns = [
    path("", listarLivros, name="listar-livros"),
    path("create", inserirLivro, name="adicionar-livro"),
]
