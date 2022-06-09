from django.urls import path
from .views import listarLivros, inserirLivro
from .views import listarLivros, inserirLivro, atualizarLivro, deletarLivro

urlpatterns = [
    path("", listarLivros, name="listar-livros"),
    path("create", inserirLivro, name="adicionar-livro"),
    path("delete/<int:id>", deletarLivro, name="deletar-livro"),
]
