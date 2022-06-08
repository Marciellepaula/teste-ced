from django.shortcuts import redirect, render
from .models import Livro
from .forms import LivroForm

# Create your views here.

def listarLivros(request):
    livros = Livro.objects.all()
    return render(request, 'listar-livros.html', {'livros': livros})

def inserirLivro(request):
    form = LivroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar-livros')
    return render(request, 'create-livro.html', {'form': form})