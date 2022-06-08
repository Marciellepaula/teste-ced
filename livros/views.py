from django.shortcuts import render
from .models import Livro

# Create your views here.

def listarLivros(request):
    livros = Livro.objects.all()
    return render(request, 'listar-livros.html', {'livros': livros})