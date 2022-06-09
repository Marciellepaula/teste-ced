from django.urls import path
from .views import listarLivros, inserirLivro, atualizarLivro, deletarLivro

urlpatterns = [
    path("", listarLivros, name="listar-livros"),
    path("create", inserirLivro, name="adicionar-livro"),
    path("edit/<int:id>", atualizarLivro, name="editar-livro"),
    path("delete/<int:id>", deletarLivro, name="deletar-livro"),
]
