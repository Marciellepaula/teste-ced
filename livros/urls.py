from django.urls import path
from .views import listarLivros

urlpatterns = [
    path("", listarLivros, name="listar-livros"),
]
